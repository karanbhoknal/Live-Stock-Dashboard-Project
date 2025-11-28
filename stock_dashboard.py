import streamlit as st
import plotly.express as px
from utils.stock_functions import get_stock_data, calculate_summary

# Page config
st.set_page_config(page_title="📈 Live Stock Dashboard", layout="wide")

# Title
st.title("📊 Live Stock Price Dashboard")

# Sidebar inputs
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
period = st.sidebar.selectbox("Select Period", ["1d","5d","1mo","3mo"])
interval = st.sidebar.selectbox("Select Interval", ["1m","5m","15m","1h","1d"])

# Fetch data
data = get_stock_data(ticker, period, interval)

# Show data
st.subheader(f"{ticker} Stock Data (Latest 10 rows)")
st.dataframe(data.tail(10))

# Plot interactive chart
st.subheader(f"📈 {ticker} Price Chart")

fig = px.line(data, x='Datetime', y='Close', title=f'{ticker} Stock Prices')
st.plotly_chart(fig, use_container_width=True)

# Show summary stats
st.subheader("📊 Summary Stats")
summary = calculate_summary(data)
st.write(summary)

# Footer
st.markdown("---")
st.markdown("Built with Python, Pandas, Plotly, yfinance & Streamlit 🚀")
