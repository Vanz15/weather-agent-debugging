import pandas as pd


def calculate_sma(data: pd.DataFrame, window: int) -> pd.Series:
    """
    Calculate Simple Moving Average for a given window.
    """
    return data["Close"].rolling(window=window).mean()


def calculate_rsi(data: pd.DataFrame, window: int = 14) -> pd.Series:
    """
    Calculate Relative Strength Index using average gains and losses.
    """
    delta = data["Close"].diff()

    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    relative_strength = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + relative_strength))

    return rsi