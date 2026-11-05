from datetime import date

import streamlit as st

import queries
from helpers import (
    building_labels,
    distinct_values,
    equipment_conditions,
    equipment_types,
    farm_labels,
    finish_insert,
    option_select,
    page_head,
    required_select,
    run_insert,
    run_query,
    show_table,
    where_clause,
)

page_head("Equipment", "All equipment")

farms = farm_labels()
filter_columns = st.columns(4)
farm_id = option_select(
    filter_columns[0], "Farm", "All farms", farms, farms, key="equipment_farm"
)
equipment_name = option_select(
    filter_columns[1],
    "Equipment",
    "All equipment",
    distinct_values("equipment_name", "Equipment"),
    key="equipment_name",
)

conditions = []
params = []
if farm_id is not None:
    conditions.append("e.farm_id = %s")
    params.append(farm_id)
if equipment_name is not None:
    conditions.append("e.equipment_name = %s")
    params.append(equipment_name)

equipment_rows = run_query(
    queries.equipment_equipment_rows.format(where=where_clause(conditions)), params
)
show_table(
    st,
    equipment_rows,
    capitalized_columns=["Type", "Condition"],
    column_config={"Price": st.column_config.NumberColumn(format="dollar")},
)

expander = st.expander("Add equipment")
form_columns = expander.columns(3)
new_farm_id = required_select(
    form_columns[0], "Farm", list(farms), farms, key="new_equipment_farm"
)
new_manufacturer = form_columns[0].text_input(
    "Manufacturer", key="new_equipment_manufacturer"
)
new_purchase_date = form_columns[0].date_input(
    "Purchase date", value=date.today(), key="new_equipment_purchased"
)
new_last_service_date = form_columns[0].date_input(
    "Last service date", value=None, key="new_equipment_service"
)
new_equipment_name = form_columns[1].text_input(
    "Equipment name", key="new_equipment_name"
)
new_model = form_columns[1].text_input("Model", key="new_equipment_model")
new_purchase_price = form_columns[1].number_input(
    "Purchase price",
    min_value=0.0,
    step=100.0,
    value=0.0,
    key="new_equipment_price",
)
buildings = building_labels(new_farm_id)
new_building_id = required_select(
    form_columns[1],
    "Building",
    [None] + list(buildings),
    buildings,
    key="new_equipment_building",
)
new_equipment_type = required_select(
    form_columns[2], "Type", equipment_types, key="new_equipment_type"
)
new_serial_number = form_columns[2].text_input(
    "Serial number", key="new_equipment_serial"
)
new_condition = required_select(
    form_columns[2],
    "Condition",
    equipment_conditions,
    key="new_equipment_condition",
)
if expander.button("Add equipment", type="primary"):
    text_values = [
        new_equipment_name,
        new_manufacturer,
        new_model,
        new_serial_number,
    ]
    if not all(value.strip() for value in text_values):
        expander.error(
            "Enter an equipment name, manufacturer, model, and serial number."
        )
    else:
        inserted = run_insert(
            expander,
            queries.equipment_inserted,
            (
                new_equipment_name.strip(),
                new_equipment_type,
                new_manufacturer.strip(),
                new_model.strip(),
                new_serial_number.strip(),
                new_purchase_date,
                new_purchase_price,
                new_condition,
                new_last_service_date,
                new_farm_id,
                new_building_id,
            ),
        )
        if inserted:
            finish_insert("Equipment added.")
