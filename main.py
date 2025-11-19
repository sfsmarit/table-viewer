import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import config


if __name__ == "__main__":

    page_title = config.PAGE_TITLE
    st.set_page_config(page_title=page_title, layout="wide")
    st.title(page_title)

    st.markdown("---")

    placeholder = st.empty()

    df = config.create_data()

    # Grid options
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(editable=True, filter=True)  # 全列フィルタ有効
    gb.configure_pagination(enabled=True)  # ページネーション
    gb.configure_side_bar()  # サイドバーでフィルタUI表示
    grid_options = gb.build()

    response = AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=False,
        theme="streamlit",
        update_mode="MODEL_CHANGED"
    )

    edited_df = response["data"]
    csv = edited_df.to_csv(index=False)

    placeholder.download_button(
        ":material/download: csv",
        data=csv,
        file_name=config.OUTPUT_CSV,
        mime="text/csv"
    )
