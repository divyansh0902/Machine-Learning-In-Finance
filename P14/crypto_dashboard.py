from matplotlib import image
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go
from PIL import Image


st.write('''
# cryptocurrency Dashboard Application
Visually show data on crypto''')
image = Image.open("C:/Users/mehak/OneDrive/Desktop/CODING/ML in Finance/P14/shutterstock_1434643079.webp")
st.image(image,use_column_width=True)

st.sidebar.header('User Input')

def get_input():
    start_date =st.sidebar.text_input("Start Date","2022-01-01")
    end_date =st.sidebar.text_input("End Date","2022-02-01")
    crypto_symbol =st.sidebar.text_input("Crypto Symbol","BTC")
    return start_date,end_date,crypto_symbol


def get_crypto_name(symbol):
    symbol = symbol.upper()
    if symbol == "BTC":
        return "Bitcoin"
    elif symbol == "ETH":
        return "Ethereum"
    elif symbol == "DOGE":
        return "Dogecoin"
    else:
        return "None"


def get_data(symbol,start,end):
    symbol = symbol.upper()
    if symbol == "BTC":
        df = pd.read_csv("C:/Users/mehak/OneDrive/Desktop/CODING/ML in Finance/P14/BTC.csv")
    elif symbol == "ETH":
        df = pd.read_csv("C:/Users/mehak/OneDrive/Desktop/CODING/ML in Finance/P14/ETH.csv")
    elif symbol == "DOGE":
        df = pd.read_csv("C:/Users/mehak/OneDrive/Desktop/CODING/ML in Finance/P14/DOGE.csv")
    else:
        df = pd.DataFrame(columns=['Date','Close','Open','Volume'])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.loc[start:end]

start,end,symbol = get_input()
df = get_data(symbol,start,end)
crypto_name =get_crypto_name(symbol)

fig = go.Figure(
    data=[go.Candlestick(
        x = df.index,
        open = df['Open'],
        high = df['High'],
        low = df['Low'],
        close = df['Close'],
        increasing_line_color = 'green',
        decreasing_line_color = 'red'
    )]
)


st.header(crypto_name+"Date")
st.write(df)

st.header(crypto_name+" Data Statistics")
st.write(df.describe())

st.header(crypto_name+" Close Price")
st.line_chart(df['Close'])

st.header(crypto_name+" Volume")
st.bar_chart(df['Volume'])

st.header(crypto_name+" Candle Stick")
st.plotly_chart(fig)