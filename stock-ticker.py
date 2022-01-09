import yfinance as yf
import streamlit as st
from datetime import date

st.write("""
# Stock Price/Volume
Shown are the stock **closing price** and ***volume*** of your stock!
""")

#define the ticker symbol
ticker_input = ''
ticker= st.text_area("Enter your ticker symbol:", ticker_input, height=25)
#get data on this ticker
ticker_data = yf.Ticker(ticker)
#get the historical prices for this ticker
today = date.today()
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end=today)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(ticker_df.Close)
st.write("""
## Volume Price
""")
st.line_chart(ticker_df.Volume)
earnings_period = st.radio(
    "Earnings Period",
    ('Total Earnings', 'Quarterly Earnings'))
if earnings_period == 'Total Earnings':
    st.write("""
    ## Total Earnings
    """)
    st.line_chart(ticker_data.earnings)
elif earnings_period == 'Quarterly Earnings':
    st.write("""
    ## Quarterly Earnings
    """)
    st.line_chart(ticker_data.quarterly_earnings)
