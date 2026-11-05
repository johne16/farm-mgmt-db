import streamlit as st

import queries
from helpers import (
    distinct_values,
    farm_labels,
    option_select,
    page_head,
    product_categories,
    run_query,
    show_table,
    where_clause,
)

page_head("Products", "Stock on hand by farm and product")

farms = farm_labels()
filter_columns = st.columns(4)
farm_id = option_select(
    filter_columns[0], "Farm", "All farms", farms, farms, key="products_farm"
)
product_category = option_select(
    filter_columns[1],
    "Product category",
    "All categories",
    product_categories,
    key="products_category",
)
product_name = option_select(
    filter_columns[2],
    "Product",
    "All products",
    distinct_values("product_name", "Products"),
    key="products_product",
)

conditions = []
params = []
if farm_id is not None:
    conditions.append("s.farm_id = %s")
    params.append(farm_id)
if product_category is not None:
    conditions.append("p.product_category = %s")
    params.append(product_category)
if product_name is not None:
    conditions.append("p.product_name = %s")
    params.append(product_name)

stock_rows = run_query(
    queries.products_stock_rows.format(where=where_clause(conditions)), params
)
show_table(
    st,
    stock_rows,
    capitalized_columns=["Category", "Unit"],
    column_config={
        "List price": st.column_config.NumberColumn(format="dollar"),
        "On hand": st.column_config.NumberColumn(format="localized"),
    },
)
