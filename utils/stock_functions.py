import yfinance as yf
import pandas as pd

def get_stock_data(ticker, period="1d", interval="5m"):
    """
    Fetch stock data using yfinance.
    ticker: stock symbol, e.g., 'AAPL'
    period: '1d', '5d', '1mo', etc.
    interval: '1m', '5m', '15m', etc.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    data.reset_index(inplace=True)
    return data

# def calculate_summary(data):
#     """
#     Return summary stats for a stock dataframe
#     """
#     summary = {
#         "Open": data['Open'].iloc[-1],
#         "Close": data['Close'].iloc[-1],
#         "High": data['High'].max(),
#         "Low": data['Low'].min(),
#         "Volume": data['Volume'].sum(),
#         "Change%": round((data['Close'].iloc[-1] - data['Open'].iloc[0]) / data['Open'].iloc[0] * 100, 2)
#     }
#     return summary

def calculate_summary(data):
    if data is None or data.empty:
        return {
            "Open": None,
            "High": None,
            "Low": None,
            "Close": None,
            "Volume": None,
            "Message": "No data available"
        }

    return {
        "Open": data['Open'].iloc[-1],
        "High": data['High'].iloc[-1],
        "Low": data['Low'].iloc[-1],
        "Close": data['Close'].iloc[-1],
        "Volume": data['Volume'].iloc[-1],
    }
