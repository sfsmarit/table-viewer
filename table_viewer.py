import streamlit as st
import data
from utils import login_form


page_title = data.PAGE_TITLE
st.set_page_config(page_title=page_title, layout="centered")
st.title(page_title)

if login_form.login():
    st.set_page_config(layout="wide")
    st.markdown("---")

    # Download button
    placeholder = st.empty()

    # Table
    df = data.create_data()
    edited_df = st.data_editor(df, width="stretch")

    csv = edited_df.to_csv(index=False)
    placeholder.download_button(
        ":material/download: csv",
        data=csv,
        file_name=data.OUTPUT_CSV,
        mime="text/csv",
    )
