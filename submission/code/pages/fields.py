from datetime import date

import streamlit as st

import queries
from helpers import (
    crop_varieties,
    distinct_values,
    farm_labels,
    finish_insert,
    growth_statuses,
    option_select,
    page_head,
    required_select,
    run_insert,
    run_query,
    show_table,
    where_clause,
)

page_head("Fields", "All plantings")

farms = farm_labels()
filter_columns = st.columns(4)
farm_id = option_select(
    filter_columns[0], "Farm", "All farms", farms, farms, key="fields_farm"
)
crop_name = option_select(
    filter_columns[1],
    "Crop",
    "All crops",
    distinct_values("crop_name", "Crops"),
    key="fields_crop",
)
variety = option_select(
    filter_columns[2],
    "Variety",
    "All varieties",
    crop_varieties(crop_name),
    key="fields_variety",
)
growth_status = option_select(
    filter_columns[3],
    "Growth status",
    "All statuses",
    growth_statuses,
    key="fields_status",
)

conditions = []
params = []
if farm_id is not None:
    conditions.append("p.farm_id = %s")
    params.append(farm_id)
if crop_name is not None:
    conditions.append("c.crop_name = %s")
    params.append(crop_name)
if variety is not None:
    conditions.append("c.variety = %s")
    params.append(variety)
if growth_status is not None:
    conditions.append("p.growth_status = %s")
    params.append(growth_status)

plantings = run_query(
    queries.fields_plantings.format(where=where_clause(conditions)), params
)
show_table(
    st,
    plantings,
    capitalized_columns=["Status"],
    column_config={"Acres": st.column_config.NumberColumn(format="%.2f")},
)

expander = st.expander("Add a planting")
crops = run_query(queries.fields_crops)
crop_labels = dict(zip(crops["crop_id"], crops["label"]))
form_columns = expander.columns(3)
new_farm_id = required_select(
    form_columns[0], "Farm", list(farms), farms, key="new_planting_farm"
)
new_planting_date = form_columns[0].date_input(
    "Planting date", value=date.today(), key="new_planting_date"
)
new_field_number = form_columns[1].number_input(
    "Field number", min_value=1, step=1, value=1, key="new_planting_field"
)
new_harvest_date = form_columns[1].date_input(
    "Expected harvest date", value=date.today(), key="new_planting_harvest"
)
new_crop_id = required_select(
    form_columns[2], "Crop", list(crop_labels), crop_labels, key="new_planting_crop"
)
new_acres = form_columns[2].number_input(
    "Acres", min_value=0.0, step=0.25, value=10.0, key="new_planting_acres"
)
if expander.button("Add planting", type="primary"):
    inserted = run_insert(
        expander,
        queries.fields_inserted,
        (
            new_field_number,
            new_acres,
            new_planting_date,
            new_harvest_date,
            new_farm_id,
            new_crop_id,
        ),
    )
    if inserted:
        finish_insert("Planting added.")
