import gspread

import pandas as pd
import numpy as np

import streamlit as st
import streamlit.web.cli as stcli
import altair as alt


def get_data_from_google_sheet():
    gc = gspread.service_account_from_dict(st.secrets["service_account"])
    wks = gc.open("CAB DataPipeline Tesla Stock Price").sheet1
    full_list_of_lists = wks.get_all_values()
    list_of_lists = full_list_of_lists[1:]
    df = pd.DataFrame(list_of_lists, columns = ['date', 'closing price', "day's high", "day's low", "opening price", "trade volume", "$ change", "% change"])
    return df

tesla_chart = get_data_from_google_sheet()

st.dataframe(tesla_chart)