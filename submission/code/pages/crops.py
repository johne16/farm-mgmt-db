import streamlit as st

import queries
from helpers import (
    crop_varieties,
    distinct_values,
    farm_labels,
    growth_statuses,
    option_select,
    page_head,
    run_query,
    show_table,
    where_clause,
)

page_head("Crops", "Total acres planted by farm, crop, and variety")

farms = farm_labels()
filter_columns = st.columns(4)
farm_id = option_select(
    filter_columns[0], "Farm", "All farms", farms, farms, key="crops_farm"
)
crop_name = option_select(
    filter_columns[1],
    "Crop",
    "All crops",
    distinct_values("crop_name", "Crops"),
    key="crops_crop",
)
variety = option_select(
    filter_columns[2],
    "Variety",
    "All varieties",
    crop_varieties(crop_name),
    key="crops_variety",
)
growth_status = option_select(
    filter_columns[3],
    "Growth status",
    "All statuses",
    growth_statuses,
    key="crops_status",
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

acres = run_query(queries.crops_acres.format(where=where_clause(conditions)), params)
show_table(
    st, acres, column_config={"Acres": st.column_config.NumberColumn(format="%.2f")}
)
