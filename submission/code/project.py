import streamlit as st

st.set_page_config(page_title="Farm management", layout="wide")

if "message" in st.session_state:
    st.toast(st.session_state.pop("message"))

navigation = st.navigation(
    {
        "": [st.Page("pages/overview.py", title="Overview", default=True)],
        "Farm": [
            st.Page("pages/fields.py", title="Fields"),
            st.Page("pages/crops.py", title="Crops"),
            st.Page("pages/livestock.py", title="Livestock"),
            st.Page("pages/equipment.py", title="Equipment"),
            st.Page("pages/workers.py", title="Workers"),
        ],
        "Money": [
            st.Page("pages/sales.py", title="Sales"),
            st.Page("pages/products.py", title="Products"),
        ],
    }
)
navigation.run()
