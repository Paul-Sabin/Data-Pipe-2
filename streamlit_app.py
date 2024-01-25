import gspread

import pandas as pd
import numpy as np
import plotly.graph_objects as go

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

tesla_chart['date'] = pd.to_datetime(tesla_chart['date'])

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=tesla_chart['date'],
                open=tesla_chart['opening price'],
                high=tesla_chart['day\'s high'],
                low=tesla_chart['day\'s low'],
                close=tesla_chart['closing price'],
                increasing_line_color='green', increasing_fillcolor='green',
                decreasing_line_color='red', decreasing_fillcolor='red')])

# Updating layout for better readability
fig.update_layout(
    title='TSLA Stock Price',
    xaxis=dict(
    tickangle=-90,
    tickformat='%d-%m',        
    tickmode='linear',
    tick0=0,
    dtick=3
    ),
    xaxis_title='Date',
    yaxis_title='Price in USD',
    xaxis_rangeslider_visible=False
)

# Display the figure in Streamlit
st.plotly_chart(fig)

st.dataframe(tesla_chart)