import streamlit as st

# import data
import saw_tapeout as data

if __name__ == "__main__":

    page_title = data.PAGE_TITLE
    st.set_page_config(page_title=page_title, layout="wide")
    st.title(page_title)

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
