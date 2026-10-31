import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

project_dir = Path(__file__).resolve().parent
environment_file = project_dir / "environment.yml"
schema_file = project_dir / "code" / "schema.sql"

env_name = "farm_mgmt"
container_name = "farm_mgmt_db"
postgres_image = "postgres:16"
db_name = "farm_mgmt"
db_user = "postgres"
db_password = "postgres"
db_port = 5432


def find_conda():
    conda_path = os.environ.get("CONDA_EXE") or shutil.which("conda")
    if not conda_path:
        sys.exit("Failed: conda was not found.")
    return conda_path


def check_docker():
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


def setup_conda_env(conda_path):
    if conda_env_exists(conda_path):
        print(f"Updating conda environment {env_name}.")
        command = [
            conda_path, "env", "update",
            "--name", env_name,
            "--file", str(environment_file),
            "--prune",
        ]
    else:
        print(f"Creating conda environment {env_name}.")
        command = [
            conda_path, "env", "create",
            "--file", str(environment_file),
        ]
    if subprocess.run(command).returncode != 0:
        sys.exit("Failed: conda environment setup did not complete.")
    print("Conda environment is ready.")


def run_postgres(docker_path):
    command = [
        docker_path, "run",
        "--rm",
        "--name", container_name,
        "-e", f"POSTGRES_USER={db_user}",
        "-e", f"POSTGRES_PASSWORD={db_password}",
        "-e", f"POSTGRES_DB={db_name}",
        "-p", f"127.0.0.1:{db_port}:5432",
        "--mount", f"type=bind,src={schema_file},dst=/docker-entrypoint-initdb.d/schema.sql",
        postgres_image,
    ]
    print(f"Starting Postgres container {container_name}. Press Ctrl+C to stop it.")
    process = subprocess.Popen(command)
    try:
        return process.wait()
    except KeyboardInterrupt:
        return process.wait()


def main():
    conda_path = find_conda()
    docker_path = check_docker()
    setup_conda_env(conda_path)
    return_code = run_postgres(docker_path)
    print(f"Postgres container stopped with exit code {return_code}.")


if __name__ == "__main__":
    main()
