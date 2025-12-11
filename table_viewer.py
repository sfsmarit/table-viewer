import streamlit as st
from utils import login_form

import data


page_title = data.PAGE_TITLE
st.set_page_config(page_title=page_title, page_icon=":rainbow_flag:", layout="wide")
st.title(page_title)


if not data.REQUIRE_AUTH or login_form.login():
    st.markdown("---")

    download_button_placeholder = st.empty()

    # Table
    df = data.create_data()
    edited_df = st.data_editor(df, width="stretch")

    csv = edited_df.to_csv(index=False)
    download_button_placeholder.download_button(
        ":material/download: csv",
        data=csv,
        file_name=data.OUTPUT_CSV,
        mime="text/csv",
    )
