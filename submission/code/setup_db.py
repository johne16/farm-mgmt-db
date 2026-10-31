import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
environment_file = project_dir / "environment.yml"
schema_file = project_dir / "code" / "schema.sql"
insertion_file = project_dir / "data" / "insertion.sql"

env_name = "farm_mgmt"
container_name = "farm_mgmt_db"
postgres_image = "postgres:16"
db_name = "farm_mgmt"
db_user = "postgres"
db_password = "postgres"
db_port = 5432
load_timeout_seconds = 120


def find_conda():
    conda_path = os.environ.get("CONDA_EXE") or shutil.which("conda")
    if not conda_path:
        sys.exit("Failed: conda was not found.")
    return conda_path


def find_docker():
    docker_path = shutil.which("docker")
    if not docker_path:
        sys.exit("Failed: docker was not found.")
    result = subprocess.run([docker_path, "info"], capture_output=True)
    if result.returncode != 0:
        sys.exit("Failed: Docker is not running.")
    return docker_path


def conda_env_exists(conda_path):
    result = subprocess.run(
        [conda_path, "env", "list", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    env_paths = json.loads(result.stdout)["envs"]
    return any(Path(env_path).name == env_name for env_path in env_paths)


def container_exists(docker_path):
    result = subprocess.run(
        [
            docker_path, "ps",
            "--all",
            "--filter", f"name={container_name}",
            "--format", "{{.Names}}",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return container_name in result.stdout.splitlines()


def create_conda_env(conda_path):
    print(f"Creating conda environment {env_name}.")
    command = [
        conda_path, "env", "create",
        "--file", str(environment_file),
    ]
    if subprocess.run(command).returncode != 0:
        sys.exit("Failed: conda environment was not created.")
    print("Conda environment created.")


def create_container(docker_path):
    print(f"Creating Postgres container {container_name}.")
    command = [
        docker_path, "create",
        "--name", container_name,
        "-e", f"POSTGRES_USER={db_user}",
        "-e", f"POSTGRES_PASSWORD={db_password}",
        "-e", f"POSTGRES_DB={db_name}",
        "-p", f"127.0.0.1:{db_port}:5432",
        "--mount", f"type=bind,src={schema_file},dst=/docker-entrypoint-initdb.d/01_schema.sql",
    ]
    if insertion_file.exists():
        command += ["--mount", f"type=bind,src={insertion_file},dst=/docker-entrypoint-initdb.d/02_insertion.sql"]
    command.append(postgres_image)
    if subprocess.run(command).returncode != 0:
        sys.exit("Failed: Postgres container was not created.")
    print("Postgres container created.")


def delete_container(docker_path):
    command = [docker_path, "rm", "--force", "--volumes", container_name]
    return subprocess.run(command, capture_output=True).returncode == 0


def stop_container(docker_path):
    command = [docker_path, "stop", container_name]
    return subprocess.run(command, capture_output=True).returncode == 0


def container_running(docker_path):
    result = subprocess.run(
        [
            docker_path, "ps",
            "--filter", f"name={container_name}",
            "--filter", "status=running",
            "--format", "{{.Names}}",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return container_name in result.stdout.splitlines()


def load_database(docker_path):
    print(f"Starting Postgres container {container_name}.")
    start_command = [docker_path, "start", container_name]
    if subprocess.run(start_command, capture_output=True).returncode != 0:
        delete_container(docker_path)
        sys.exit("Failed: Postgres container did not start.")
    print("Loading schema and data.")
    ready_command = [
        docker_path, "exec", container_name,
        "pg_isready", "-q",
        "-h", "127.0.0.1",
        "-U", db_user,
        "-d", db_name,
    ]
    deadline = time.monotonic() + load_timeout_seconds
    try:
        while subprocess.run(ready_command, capture_output=True).returncode != 0:
            if not container_running(docker_path) or time.monotonic() > deadline:
                subprocess.run([docker_path, "logs", container_name])
                delete_container(docker_path)
                sys.exit("Failed: schema and data were not loaded.")
            time.sleep(1)
    except KeyboardInterrupt:
        delete_container(docker_path)
        sys.exit("Failed: setup was interrupted.")
    print("Schema and data loaded.")


def main():
    conda_path = find_conda()
    docker_path = find_docker()
    if conda_env_exists(conda_path):
        print(f"Conda environment {env_name} already exists.")
    else:
        create_conda_env(conda_path)
    if container_exists(docker_path):
        print(f"Postgres container {container_name} already exists.")
        if not container_running(docker_path):
            print(f"Starting Postgres container {container_name}.")
            start_command = [docker_path, "start", container_name]
            if subprocess.run(start_command, capture_output=True).returncode != 0:
                sys.exit("Failed: Postgres container did not start.")
    else:
        create_container(docker_path)
        load_database(docker_path)
    print("Setup complete.")


if __name__ == "__main__":
    main()
