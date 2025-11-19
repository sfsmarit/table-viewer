import streamlit as st
import pandas as pd


PAGE_TITLE = "Table Viewer"
OUTPUT_CSV = "data.csv"
CACHE_TIME = 1  # [s]


@st.cache_data(ttl=CACHE_TIME)
def create_data() -> pd.DataFrame:
    df = pd.DataFrame({
        "Name": ["Tanaka", "Yamada"],
        "Age": [30, 40],
    })
    return df
