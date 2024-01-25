# I think the whole idea behind this script is wrong. My streamlit app is not a Lambda function.
import gspread

import pandas as pd
import numpy as np

import streamlit as st
import streamlit.web.cli as stcli
import altair as alt


def get_data():
    gc = gspread.service_account(filename="./service_account.json")
    wks = gc.open("CAB DataPipeline Tesla Stock Price").sheet1
    full_list_of_lists = wks.get_all_values()
    list_of_lists = full_list_of_lists[1:]
    df = pd.DataFrame(list_of_lists, columns = ['date', 'price'])
    return df

tesla_chart = get_data()

st.line_chart(tesla_chart, x="date", y="price")