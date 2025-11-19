import streamlit as st

import config


if __name__ == "__main__":

    page_title = config.PAGE_TITLE
    st.set_page_config(page_title=page_title, layout="wide")
    st.title(page_title)

    st.markdown("---")

    placeholder = st.empty()

    df = config.create_data()
    new_df = st.data_editor(
        df,
        width="stretch",
    )

    csv = new_df.to_csv(index=False)

    placeholder.download_button(
        ":material/download: csv",
        data=csv,
        file_name=config.OUTPUT_CSV,
        mime="text/csv"
    )
