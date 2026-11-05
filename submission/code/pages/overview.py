from datetime import date

import streamlit as st

import queries
from helpers import capitalize_first, page_head, run_query, show_table

today = date.today()
page_head("Overview", f"{today:%A, %B} {today.day}")

bills = run_query(queries.overview_bills)
orders_to_ship = run_query(queries.overview_orders_to_ship)
fields_to_harvest = run_query(queries.overview_fields_to_harvest)
animals_needing_care = run_query(queries.overview_animals_needing_care)

metric_columns = st.columns(4)
metric_columns[0].metric(
    "Unpaid bills",
    f"${bills['owed'][0]:,.0f}",
    delta=f"{bills['past_due'][0]} past due",
    delta_color="inverse",
    delta_arrow="off",
    border=True,
)
metric_columns[1].metric(
    "Orders to ship", int(orders_to_ship["total"][0]), border=True
)
metric_columns[2].metric(
    "Fields to harvest", int(fields_to_harvest["total"][0]), border=True
)
metric_columns[3].metric(
    "Animals needing care", int(animals_needing_care["total"][0]), border=True
)

left_column, right_column = st.columns([3, 2], gap="large")

left_column.subheader("Upcoming harvests")
harvests = run_query(queries.overview_harvests)
show_table(
    left_column,
    harvests,
    column_config={"Acres": st.column_config.NumberColumn(format="%.2f")},
)

right_column.subheader("Sales by customer type")
sales = run_query(queries.overview_sales)
sales["Customer type"] = sales["Customer type"].map(capitalize_first)
right_column.bar_chart(
    sales,
    x="Customer type",
    y="Total sales",
    x_label="",
    y_label="Total sales ($)",
    color="primary",
    horizontal=True,
    sort="-Total sales",
)
