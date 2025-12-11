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
        "website": ["https://ja.wikipedia.org/", "https://www.youtube.com/"],
    })
    return df
```

If your table contains url and you want to activate the link, specify the columns as;
```python
# data.py
def linked_columns() -> list[str]:
    return ["website"]
```

Run;
```bash
streamlit run main.py
```