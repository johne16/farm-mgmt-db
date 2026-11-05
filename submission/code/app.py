import json
import subprocess
import sys
from pathlib import Path

import setup_db

app_file = Path(__file__).resolve()
project_file = setup_db.project_dir / "code" / "project.py"
watch_argument = "--watch"


def start_watcher():
    command = [sys.executable, str(app_file), watch_argument]
    if sys.platform == "win32":
        flags = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW
        return subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=flags,
        )
    return subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )


def watch():
    sys.stdin.read()
    docker_path = setup_db.find_docker()
    setup_db.stop_container(docker_path)


def get_activated_environment(conda_path):
    command = [
        conda_path, "run",
        "-n", setup_db.env_name,
        "python", "-c",
        "import json, os, sys; print(json.dumps({'executable': sys.executable, 'environment': dict(os.environ)}))",
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit("Failed: conda environment was not activated.")
    return json.loads(result.stdout)


def start_streamlit(activated_environment):
    command = [
        activated_environment["executable"], "-m",
        "streamlit", "run", str(project_file),
    ]
    return subprocess.Popen(
        command,
        cwd=setup_db.project_dir,
        env=activated_environment["environment"],
    )


def wait_for_exit(process):
    while True:
        try:
            return process.wait()
        except KeyboardInterrupt:
            pass


def main():
    setup_db.main()
    conda_path = setup_db.find_conda()
    activated_environment = get_activated_environment(conda_path)
    print("Starting container watcher.")
    watcher_process = start_watcher()
    print("Starting Streamlit server.")
    streamlit_process = start_streamlit(activated_environment)
    wait_for_exit(streamlit_process)
    print("Streamlit server stopped.")


if __name__ == "__main__":
    if watch_argument in sys.argv:
        watch()
    else:
        main()
