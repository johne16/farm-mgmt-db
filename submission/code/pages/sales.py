from datetime import date

import streamlit as st

import queries
from helpers import (
    farm_labels,
    option_select,
    page_head,
    product_categories,
    run_query,
    show_table,
    where_clause,
)

page_head("Sales", "Delivered orders")

farms = farm_labels()
filter_columns = st.columns(4)
farm_id = option_select(
    filter_columns[0], "Farm", "All farms", farms, farms, key="sales_farm"
)
from_date = filter_columns[1].date_input(
    "From", value=date(date.today().year, 1, 1), key="sales_from"
)
to_date = filter_columns[2].date_input("To", value=date.today(), key="sales_to")
product_category = option_select(
    filter_columns[3],
    "Product category",
    "All categories",
    product_categories,
    key="sales_category",
)

conditions = [
    "o.order_status = 'delivered'",
    "o.delivery_date >= %s",
    "o.delivery_date <= %s",
]
params = [from_date, to_date]
if farm_id is not None:
    conditions.append("o.farm_id = %s")
    params.append(farm_id)
if product_category is not None:
    conditions.append("p.product_category = %s")
    params.append(product_category)

sales_rows = run_query(
    queries.sales_sales_rows.format(where=where_clause(conditions)), params
)

left_column, right_column = st.columns([3, 2], gap="large")

left_column.subheader("By farm and customer type")
show_table(
    left_column,
    sales_rows,
    capitalized_columns=["Customer type"],
    column_config={
        "Average order": st.column_config.NumberColumn(format="dollar"),
        "Total sales": st.column_config.NumberColumn(format="dollar"),
    },
)

right_column.subheader("Total sales")
totals = sales_rows.groupby("Customer type", as_index=False)["Total sales"].sum()
right_column.bar_chart(
    totals,
    x="Customer type",
    y="Total sales",
    x_label="",
    y_label="Total sales ($)",
    color="primary",
    horizontal=True,
    sort="-Total sales",
)
