import sys

import setup_db


def main():
    docker_path = setup_db.find_docker()
    if setup_db.container_exists(docker_path):
        print(f"Deleting Postgres container {setup_db.container_name}.")
        if not setup_db.delete_container(docker_path):
            sys.exit("Failed: Postgres container was not deleted.")
        print("Postgres container deleted.")
    setup_db.main()
    print(f"Stopping Postgres container {setup_db.container_name}.")
    if not setup_db.stop_container(docker_path):
        sys.exit("Failed: Postgres container was not stopped.")
    print("Postgres container stopped.")


if __name__ == "__main__":
    main()
