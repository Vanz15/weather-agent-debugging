from typing import Any, Dict, Optional
from typing_extensions import TypedDict


class StockAgentState(TypedDict):
    """
    State schema for the Stock Market Analysis Agent.

    Fields:
        ticker: User-provided stock ticker symbol.
        stock_data: Historical stock price data.
        indicators: Calculated technical indicators.
        recommendation: BUY, HOLD, or SELL recommendation.
        report: Final formatted analysis report.
        error: Error message if something fails.
    """

    ticker: str
    stock_data: Optional[Any]
    indicators: Optional[Dict[str, Any]]
    recommendation: Optional[str]
    report: Optional[str]
    error: Optional[str]