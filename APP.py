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
st.dataframe(data)
st.write("my first web")



# Everything is accessible via the st.secrets dict:
import mysql.connector
server = "rm-uf6k846wp4uld2q73po.mysql.rds.aliyuncs.com"
users = "jhyani"
pword = "Yjh950125"
database = "nongji"

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(host=server,port=3306,database="nongji",user="jhyani",password="Yjh950125")

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from test1;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
