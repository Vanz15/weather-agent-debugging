import unittest
from unittest.mock import patch
import pandas as pd

from graph import stock_agent
from components.indicators import calculate_sma, calculate_rsi


def sample_stock_data():
    dates = pd.date_range(start="2026-01-01", periods=30, freq="D")

    close_prices = [
        100, 101, 102, 103, 104,
        105, 106, 107, 108, 109,
        110, 111, 112, 113, 114,
        115, 116, 117, 118, 119,
        120, 121, 122, 123, 124,
        125, 126, 127, 128, 129,
    ]

    return pd.DataFrame(
        {
            "Open": close_prices,
            "High": close_prices,
            "Low": close_prices,
            "Close": close_prices,
            "Volume": [1000000] * 30,
        },
        index=dates,
    )


class MockTicker:
    def __init__(self, ticker):
        self.ticker = ticker

    def history(self, period="60d", interval="1d"):
        return sample_stock_data()


class EmptyMockTicker:
    def __init__(self, ticker):
        self.ticker = ticker

    def history(self, period="60d", interval="1d"):
        return pd.DataFrame()


class StockAgentTests(unittest.TestCase):
    def test_sma_calculation(self):
        data = sample_stock_data()
        sma_10 = calculate_sma(data, 10)

        self.assertEqual(round(sma_10.iloc[-1], 2), 124.5)

    def test_rsi_calculation_exists(self):
        data = sample_stock_data()
        rsi = calculate_rsi(data, 14)

        self.assertFalse(pd.isna(rsi.iloc[-1]))

    @patch("components.nodes.yf.Ticker", MockTicker)
    def test_stock_agent_generates_report(self):
        final_state = stock_agent.invoke(
            {
                "ticker": "aapl",
                "stock_data": None,
                "indicators": None,
                "recommendation": None,
                "report": None,
                "error": None,
            }
        )

        report = final_state["report"]

        self.assertIn("Ticker Symbol: AAPL", report)
        self.assertIn("Technical Indicators:", report)
        self.assertIn("Current Price", report)
        self.assertIn("SMA (10-Day)", report)
        self.assertIn("SMA (20-Day)", report)
        self.assertIn("RSI (14-Day)", report)
        self.assertIn("Recommendation:", report)

    @patch("components.nodes.yf.Ticker", EmptyMockTicker)
    def test_invalid_ticker_raises_error(self):
        with self.assertRaisesRegex(Exception, "No stock data found"):
            stock_agent.invoke(
                {
                    "ticker": "INVALIDTICKER",
                    "stock_data": None,
                    "indicators": None,
                    "recommendation": None,
                    "report": None,
                    "error": None,
                }
            )


if __name__ == "__main__":
    unittest.main()