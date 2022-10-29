import streamlit as st
import pandas as pd
import json
import mysql.connector

st.set_page_config(
    page_title="YoungYan",
    page_icon="🌱",
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



# sqlserver information:
with open('/root/RemoteWorking/.vscode/mysql.json', encoding = 'utf-8') as a:
    data = json.load(a)


# Initialize connection.
# Uses st.experimental_singleton to only run once.

@st.experimental_singleton
def init_connection():    
    return mysql.connector.connect(**data['sql_server'])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=6)
def run_query(query):
    ##with conn.cursor() as cur:
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()

rows = run_query("SELECT * from test1;")

# Print results.
data = "%-20s%-20s%-20s%-20s\n"%("TYPE","CAD","DATATYPE","MAPPING")
for row in rows:
    data += "%-20s%-20s%-20s%-20s\n"%(row[0],row[1],row[2],row[3])

st.code(data)