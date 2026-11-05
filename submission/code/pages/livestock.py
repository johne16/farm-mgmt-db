from datetime import date

import streamlit as st

import queries
from helpers import (
    building_labels,
    distinct_values,
    farm_labels,
    finish_insert,
    health_statuses,
    option_select,
    page_head,
    purposes,
    required_select,
    run_insert,
    run_query,
    sexes,
    show_table,
    where_clause,
)

page_head("Livestock", "Total animals by farm, species, and breed")

farms = farm_labels()
filter_columns = st.columns(5)
farm_id = option_select(
    filter_columns[0], "Farm", "All farms", farms, farms, key="livestock_farm"
)
species = option_select(
    filter_columns[1],
    "Species",
    "All species",
    distinct_values("species", "Animals"),
    key="livestock_species",
)
breed = option_select(
    filter_columns[2],
    "Breed",
    "All breeds",
    distinct_values("breed", "Animals"),
    key="livestock_breed",
)
health_status = option_select(
    filter_columns[3],
    "Health status",
    "All statuses",
    health_statuses,
    key="livestock_health",
)
purpose = option_select(
    filter_columns[4], "Purpose", "All purposes", purposes, key="livestock_purpose"
)

conditions = []
params = []
if farm_id is not None:
    conditions.append("a.farm_id = %s")
    params.append(farm_id)
if species is not None:
    conditions.append("a.species = %s")
    params.append(species)
if breed is not None:
    conditions.append("a.breed = %s")
    params.append(breed)
if health_status is not None:
    conditions.append("a.health_status = %s")
    params.append(health_status)
if purpose is not None:
    conditions.append("a.purpose = %s")
    params.append(purpose)

animals = run_query(
    queries.livestock_animals.format(where=where_clause(conditions)), params
)
show_table(st, animals)

expander = st.expander("Add an animal")
form_columns = expander.columns(3)
new_farm_id = required_select(
    form_columns[0], "Farm", list(farms), farms, key="new_animal_farm"
)
new_sex = required_select(form_columns[0], "Sex", sexes, key="new_animal_sex")
new_health_status = required_select(
    form_columns[0], "Health status", health_statuses, key="new_animal_health"
)
buildings = building_labels(new_farm_id)
new_building_id = required_select(
    form_columns[0],
    "Building",
    [None] + list(buildings),
    buildings,
    key="new_animal_building",
)
new_species = form_columns[1].text_input("Species", key="new_animal_species")
new_birth_date = form_columns[1].date_input(
    "Birth date", value=date.today(), key="new_animal_birth"
)
new_acquisition_date = form_columns[1].date_input(
    "Acquisition date", value=date.today(), key="new_animal_acquired"
)
new_move_in_date = form_columns[1].date_input(
    "Move-in date", value=None, key="new_animal_move_in"
)
new_breed = form_columns[2].text_input("Breed", key="new_animal_breed")
new_weight = form_columns[2].number_input(
    "Weight (lbs)", min_value=0.0, step=0.5, value=0.0, key="new_animal_weight"
)
new_purpose = required_select(
    form_columns[2], "Purpose", purposes, key="new_animal_purpose"
)
if expander.button("Add animal", type="primary"):
    if not new_species.strip() or not new_breed.strip():
        expander.error("Enter a species and a breed.")
    else:
        inserted = run_insert(
            expander,
            queries.livestock_inserted,
            (
                new_species.strip(),
                new_breed.strip(),
                new_sex,
                new_birth_date,
                new_weight,
                new_health_status,
                new_acquisition_date,
                new_purpose,
                new_farm_id,
                new_building_id,
                new_move_in_date,
            ),
        )
        if inserted:
            finish_insert("Animal added.")
