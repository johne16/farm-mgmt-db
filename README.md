# Farm Management Database Project

## submission/

Everything that goes in the zip file. See `submission/README.md` for how to run it.

- `environment.yml`: conda environment
- `.streamlit/config.toml`: Streamlit theme
- `code/app.py`: main entry point; runs setup, starts Streamlit, and stops the container when the app exits
- `code/setup_db.py`: creates the conda environment and Postgres container, loads the data, and starts the container
- `code/reset_db.py`: restores the database to the original data
- `code/project.py`: Streamlit navigation
- `code/pages/`: one file per app page
- `code/helpers.py`: database connection and shared page functions
- `code/queries.py`: SQL queries used by the pages and helpers
- `code/schema.sql`: table definitions
- `data/insertion.sql`: synthetic data loaded into the tables

## mockups/

- `ui_mockup_a.html`: sidebar layout, with all tabs built

Open either file in a browser.

## docs/

- `Project_part1_design.pdf`: part 1 assignment
- `Project_part2_implementation.pdf`: part 2 assignment
- `Activity2_1008_project_design.pdf`: project design activity

## Part 1 files

- `part1.docx`: part 1 write-up
- `part1.zip`: part 1 submission
- `schema.md`: schema notes
- `Farm_mgmt_db_er_diagram.drawio.svg`: ER diagram
- `er_diagram_draft.svg`: earlier ER diagram draft
- `application_description_draft.txt`: application description draft
