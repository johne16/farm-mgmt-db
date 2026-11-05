# Farm Management Database

## Requirements

Install both of these directly on your computer:

1. **[Docker Desktop](https://docs.docker.com/get-docker/)**. Open it and leave it running while you use the app.
2. **[Anaconda or Miniconda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html)**. This is a normal program installed on your computer, **not a Docker container**. The app creates its own Docker container for the database.

Run every command in this file from a terminal where the `conda` command works. If you have not set up conda in your regular terminal, use the one the installer provides:

- Windows: **Anaconda Prompt** from the Start menu.
- Mac: **Terminal**.

To check that both are ready, run:

```
conda --version
docker info
```

Both commands should print without errors.

## Running the app

From this folder, run:

```
python code/app.py
```

The first run creates everything the app needs and loads the data, which takes a few minutes. Later runs skip those steps.

The app opens in your browser at http://localhost:8501.

To stop the app, press `Ctrl+C` or close the terminal window. **This stops all processes the app started, including the database container.** Database changes are kept for the next run.

## Starting the database

**`app.py` already runs `setup_db.py`, so it does not need to be run on its own.**

To start only the database, run this from this folder:

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
