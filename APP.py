import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="YoungYan",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

data = pd.read_csv('./CPI_农村.csv')
st.df(data)
st.write("my first web")
