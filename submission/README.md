# Farm Management Database

## Requirements

- [Docker](https://docs.docker.com/get-docker/), running
- [Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html)

## Running the app (not built yet)

From this folder, run:

```
python code/app.py
```

The first run creates everything the app needs and loads the data, which takes a few minutes. Later runs skip those steps.

To stop the app, press `Ctrl+C` or close the terminal window. Database changes are kept for the next run.

## Starting the database

From this folder, run:

```
python code/setup_db.py
```

The first run creates the conda environment and Postgres container and loads the data, which takes a few minutes. Later runs skip those steps and start the existing container.

The container keeps running after the script finishes. To stop it, run:

```
docker stop farm_mgmt_db
```

Database changes are kept for the next run.

## Resetting the database

To restore the original data, stop the app and run:

```
python code/reset_db.py
```

This erases all changes made through the app and leaves the container stopped.
