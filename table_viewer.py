import streamlit as st
from utils import login_form

import data


page_title = data.PAGE_TITLE
st.set_page_config(page_title=page_title, page_icon=":rainbow_flag:", layout="wide")
st.title(page_title)


if not data.REQUIRE_AUTH or login_form.login():
    st.markdown("---")

    download_button_placeholder = st.empty()

    df = data.create_data()

    # Table
    # Make "url" column to clickable icon
    column_config = {
        col: st.column_config.LinkColumn(label=col, display_text=":material/open_in_new:")
        for col in data.linked_columns()
    }
    st.data_editor(
        df,
        width="stretch",
        column_config=column_config,
    )

    # Download button
    download_button_placeholder.download_button(
        ":material/download: csv",
        data=df.to_csv(index=False),
        file_name=data.OUTPUT_CSV,
        mime="text/csv",
    )
