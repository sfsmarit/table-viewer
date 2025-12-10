# table-viewer
A streamlit application to view table data

## Demo Page
https://table-viewer.streamlit.app/

## Usage
Open data.py and customize create_data() method;
```python
# data.py
@st.cache_data(ttl=CACHE_TIME)
def create_data() -> pd.DataFrame:
    df = pd.DataFrame({
        "Name": ["Tanaka", "Yamada"],
        "Age": [30, 40],
    })
    return df
```

Run;
```bash
streamlit run main.py
```