from datetime import date

import streamlit as st

import queries
from helpers import (
    employment_types,
    farm_labels,
    finish_insert,
    job_titles,
    option_select,
    page_head,
    required_select,
    run_insert,
    run_query,
    show_table,
    where_clause,
)

page_head("Workers", "All workers")

farms = farm_labels()
worker_names = run_query(queries.workers_worker_names)
worker_labels = dict(zip(worker_names["worker_id"], worker_names["label"]))
filter_columns = st.columns(4)
farm_id = option_select(
    filter_columns[0], "Farm", "All farms", farms, farms, key="workers_farm"
)
worker_id = option_select(
    filter_columns[1],
    "Worker",
    "All workers",
    worker_labels,
    worker_labels,
    key="workers_name",
)

conditions = []
params = []
if farm_id is not None:
    conditions.append("w.farm_id = %s")
    params.append(farm_id)
if worker_id is not None:
    conditions.append("w.worker_id = %s")
    params.append(worker_id)

worker_rows = run_query(
    queries.workers_worker_rows.format(where=where_clause(conditions)), params
)
show_table(
    st,
    worker_rows,
    capitalized_columns=["Job title", "Employment type"],
    column_config={"Hourly wage": st.column_config.NumberColumn(format="dollar")},
)

expander = st.expander("Add a worker")
form_columns = expander.columns(3)
new_farm_id = required_select(
    form_columns[0], "Farm", list(farms), farms, key="new_worker_farm"
)
new_hire_date = form_columns[0].date_input(
    "Hire date", value=date.today(), key="new_worker_hired"
)
new_phone = form_columns[0].text_input("Phone", key="new_worker_phone")
new_first_name = form_columns[1].text_input("First name", key="new_worker_first")
new_hourly_wage = form_columns[1].number_input(
    "Hourly wage", min_value=0.0, step=0.25, value=18.0, key="new_worker_wage"
)
new_email = form_columns[1].text_input("Email", key="new_worker_email")
new_last_name = form_columns[2].text_input("Last name", key="new_worker_last")
new_employment_type = required_select(
    form_columns[2], "Employment type", employment_types, key="new_worker_type"
)
new_job_title = required_select(
    form_columns[2], "Job title", job_titles, key="new_worker_title"
)
if expander.button("Add worker", type="primary"):
    text_values = [new_first_name, new_last_name, new_phone, new_email]
    if not all(value.strip() for value in text_values):
        expander.error("Enter a first name, last name, phone, and email.")
    else:
        inserted = run_insert(
            expander,
            queries.workers_inserted,
            (
                new_first_name.strip(),
                new_last_name.strip(),
                new_job_title,
                new_hire_date,
                new_hourly_wage,
                new_employment_type,
                new_phone.strip(),
                new_email.strip(),
                new_farm_id,
            ),
        )
        if inserted:
            finish_insert("Worker added.")
