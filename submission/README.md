# Farm Management Database

## Requirements

- [Docker](https://docs.docker.com/get-docker/), running
- [Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html)

## Running the app

From this folder, run:

```
python code/app.py
```

The first run creates everything the app needs and loads the data, which takes a few minutes. Later runs skip those steps.

To stop the app, press `Ctrl+C` or close the terminal window. Database changes are kept for the next run.

## Resetting the database

To restore the original data, stop the app and run:

```
python code/reset_db.py
```

This erases all changes made through the app.
