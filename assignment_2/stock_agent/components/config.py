from dataclasses import dataclass


@dataclass(frozen=True)
class StockAgentConfig:
    """
    Configuration values for the Stock Market Analysis Agent.
    """

    period: str = "60d"
    interval: str = "1d"

    sma_short_window: int = 10
    sma_long_window: int = 20
    rsi_window: int = 14

    rsi_oversold_threshold: float = 30.0
    rsi_overbought_threshold: float = 70.0


config = StockAgentConfig()