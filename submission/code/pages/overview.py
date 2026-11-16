import html
import textwrap
from datetime import date

import streamlit as st

import queries
from helpers import capitalize_first, page_head, run_query, show_table

today = date(2026, 10, 31)
page_head("Overview", f"{today:%A, %B} {today.day}")

bills = run_query(queries.overview_bills)
orders_to_ship = run_query(queries.overview_orders_to_ship)
fields_to_harvest = run_query(queries.overview_fields_to_harvest)
animals_needing_care = run_query(queries.overview_animals_needing_care)

flip_card_style = """
<style>
.flip-cards {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1rem;
}
.flip-card {
    display: block;
    height: 150px;
    perspective: 1000px;
    cursor: pointer;
}
.flip-card input {
    display: none;
}
.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.5s;
    transform-style: preserve-3d;
}
.flip-card input:checked + .flip-card-inner {
    transform: rotateY(180deg);
}
.flip-card-front,
.flip-card-back {
    position: absolute;
    inset: 0;
    box-sizing: border-box;
    padding: 1rem;
    border: 1px solid #cbd6c6;
    border-radius: 4px;
    background: #f6f8f3;
    color: #1c2a21;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
}
.flip-card-back {
    transform: rotateY(180deg);
    overflow: auto;
    background: #e7ede2;
}
.flip-card-back pre {
    margin: 0;
    font-size: 11px;
    white-space: pre-wrap;
}
.flip-card-label {
    font-size: 14px;
}
.flip-card-value {
    margin-top: 0.25rem;
    font-size: 2.25rem;
    line-height: 1.2;
}
.flip-card-delta {
    display: inline-block;
    margin-top: 0.25rem;
    padding: 0 0.4rem;
    border-radius: 4px;
    font-size: 14px;
    color: #b3261e;
    background: rgba(179, 38, 30, 0.1);
}
</style>
"""


def flip_card(label, value, query, delta=None):
    delta_html = (
        f'<div class="flip-card-delta">{html.escape(delta)}</div>' if delta else ""
    )
    query_text = html.escape(textwrap.dedent(query).strip())
    return (
        '<label class="flip-card"><input type="checkbox">'
        '<div class="flip-card-inner">'
        f'<div class="flip-card-front"><div class="flip-card-label">{html.escape(label)}</div>'
        f'<div class="flip-card-value">{html.escape(value)}</div>{delta_html}</div>'
        f'<div class="flip-card-back"><pre>{query_text}</pre></div>'
        "</div></label>"
    )


st.html(flip_card_style)
st.html(
    '<div class="flip-cards">'
    + flip_card(
        "Unpaid bills",
        f"${bills['owed'][0]:,.0f}",
        queries.overview_bills,
        delta=f"{bills['past_due'][0]} past due",
    )
    + flip_card(
        "Orders to ship",
        str(int(orders_to_ship["total"][0])),
        queries.overview_orders_to_ship,
    )
    + flip_card(
        "Fields to harvest",
        str(int(fields_to_harvest["total"][0])),
        queries.overview_fields_to_harvest,
    )
    + flip_card(
        "Animals needing care",
        str(int(animals_needing_care["total"][0])),
        queries.overview_animals_needing_care,
    )
    + "</div>"
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
