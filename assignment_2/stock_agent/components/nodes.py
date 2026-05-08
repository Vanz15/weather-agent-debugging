import yfinance as yf
import pandas as pd

from components.state import StockAgentState
from components.config import config
from components.indicators import calculate_sma, calculate_rsi


def validate_ticker(state: StockAgentState) -> StockAgentState:
    """
    Validate user-provided ticker symbol.
    """
    ticker = state["ticker"].strip().upper()

    if not ticker:
        raise ValueError("Ticker symbol cannot be empty.")

    state["ticker"] = ticker
    return state


def fetch_stock_data(state: StockAgentState) -> StockAgentState:
    """
    Fetch 60 days of historical stock data using yfinance.
    """
    ticker = state["ticker"]

    try:
        stock = yf.Ticker(ticker)

        data = stock.history(
            period=config.period,
            interval=config.interval
        )

        if data.empty:
            raise ValueError(f"No stock data found for ticker: {ticker}")

        state["stock_data"] = data
        return state

    except Exception as error:
        raise Exception(f"Failed to fetch stock data: {error}")


def calculate_indicators_node(state: StockAgentState) -> StockAgentState:
    """
    Calculate technical indicators.
    """
    data: pd.DataFrame = state["stock_data"]

    data["SMA_10"] = calculate_sma(
        data,
        config.sma_short_window
    )

    data["SMA_20"] = calculate_sma(
        data,
        config.sma_long_window
    )

    data["RSI_14"] = calculate_rsi(
        data,
        config.rsi_window
    )

    latest = data.iloc[-1]

    indicators = {
        "current_price": round(latest["Close"], 2),
        "sma_10": round(latest["SMA_10"], 2),
        "sma_20": round(latest["SMA_20"], 2),
        "rsi_14": round(latest["RSI_14"], 2),
    }

    state["indicators"] = indicators
    state["stock_data"] = data

    return state


def generate_recommendation(state: StockAgentState) -> StockAgentState:
    """
    Generate BUY/HOLD/SELL recommendation.
    """
    indicators = state["indicators"]

    price = indicators["current_price"]
    sma_10 = indicators["sma_10"]
    sma_20 = indicators["sma_20"]
    rsi = indicators["rsi_14"]

    recommendation = "HOLD"

    if (
        price > sma_10
        and sma_10 > sma_20
        and rsi < config.rsi_overbought_threshold
    ):
        recommendation = "BUY"

    elif (
        price < sma_10
        and sma_10 < sma_20
        and rsi > config.rsi_oversold_threshold
    ):
        recommendation = "SELL"

    state["recommendation"] = recommendation

    return state


def format_report(state: StockAgentState) -> StockAgentState:
    """
    Create formatted stock analysis report.
    """
    ticker = state["ticker"]
    indicators = state["indicators"]
    recommendation = state["recommendation"]

    report = f"""
========================================
Stock Market Analysis Report
========================================

Ticker Symbol: {ticker}

Technical Indicators:
- Current Price: ${indicators['current_price']}
- SMA (10-Day): ${indicators['sma_10']}
- SMA (20-Day): ${indicators['sma_20']}
- RSI (14-Day): {indicators['rsi_14']}

Recommendation:
>>> {recommendation}

========================================
"""

    state["report"] = report.strip()

    return state