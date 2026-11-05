import pandas as pd
import psycopg2
import psycopg2.extensions
import streamlit as st

import queries
import setup_db

growth_statuses = ["planted", "growing", "harvested"]
health_statuses = ["healthy", "sick", "injured", "under treatment"]
purposes = ["dairy", "meat", "breeding", "eggs"]
sexes = ["female", "male"]
equipment_types = ["tractor", "harvester", "irrigation", "trailer"]
equipment_conditions = ["operational", "in repair", "retired"]
job_titles = [
    "equipment operator",
    "livestock handler",
    "field hand",
    "mechanic",
    "manager",
]
employment_types = ["full time", "part time", "seasonal"]
product_categories = ["produce", "grain", "dairy", "meat", "eggs", "livestock"]

decimal_to_float = psycopg2.extensions.new_type(
    psycopg2.extensions.DECIMAL.values,
    "DECIMAL_TO_FLOAT",
    lambda value, cursor: float(value) if value is not None else None,
)
psycopg2.extensions.register_type(decimal_to_float)


@st.cache_resource
def get_connection():
    connection = psycopg2.connect(
        host="127.0.0.1",
        port=setup_db.db_port,
        dbname=setup_db.db_name,
        user=setup_db.db_user,
        password=setup_db.db_password,
    )
    connection.autocommit = True
    return connection


def run_query(query, params=None):
    with get_connection().cursor() as cursor:
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        return pd.DataFrame(cursor.fetchall(), columns=columns)


def run_insert(container, query, params):
    try:
        with get_connection().cursor() as cursor:
            cursor.execute(query, params)
    except psycopg2.Error as error:
        container.error(f"Failed: {error.pgerror or error}")
        return False
    return True


def capitalize_first(value):
    return value[:1].upper() + value[1:]


def where_clause(conditions):
    if not conditions:
        return ""
    return "where " + " and ".join(conditions)


def show_table(container, df, capitalized_columns=(), column_config=None):
    for column in capitalized_columns:
        df[column] = df[column].map(capitalize_first)
    container.dataframe(df, hide_index=True, column_config=column_config)


def option_select(container, label, all_label, options, labels=None, key=None):
    def format_option(option):
        if option is None:
            return all_label
        if labels is not None:
            return labels[option]
        return capitalize_first(str(option))

    return container.selectbox(
        label, [None] + list(options), format_func=format_option, key=key
    )


def required_select(container, label, options, labels=None, key=None):
    def format_option(option):
        if option is None:
            return "None"
        if labels is not None:
            return labels[option]
        return capitalize_first(str(option))

    return container.selectbox(label, options, format_func=format_option, key=key)


def farm_labels():
    farms = run_query(queries.farm_labels_farms)
    return dict(zip(farms["farm_id"], farms["farm_name"]))


def building_labels(farm_id):
    buildings = run_query(queries.building_labels_buildings, (farm_id,))
    return dict(zip(buildings["building_id"], buildings["label"]))


def distinct_values(column, table):
    values = run_query(
        queries.distinct_values_values.format(column=column, table=table)
    )
    return values[column].tolist()


def crop_varieties(crop_name):
    if crop_name is None:
        return distinct_values("variety", "Crops")
    varieties = run_query(queries.crop_varieties_varieties, (crop_name,))
    return varieties["variety"].tolist()


def page_head(title, caption):
    st.title(title)
    st.caption(caption)


def finish_insert(message):
    st.session_state.message = message
    st.rerun()
