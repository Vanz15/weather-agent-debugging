from langgraph.graph import StateGraph, START, END

from components.state import StockAgentState
from components.nodes import (
    validate_ticker,
    fetch_stock_data,
    calculate_indicators_node,
    generate_recommendation,
    format_report,
)


builder = StateGraph(StockAgentState)

builder.add_node("validate_ticker", validate_ticker)
builder.add_node("fetch_stock_data", fetch_stock_data)
builder.add_node("calculate_indicators", calculate_indicators_node)
builder.add_node("generate_recommendation", generate_recommendation)
builder.add_node("format_report", format_report)

builder.add_edge(START, "validate_ticker")
builder.add_edge("validate_ticker", "fetch_stock_data")
builder.add_edge("fetch_stock_data", "calculate_indicators")
builder.add_edge("calculate_indicators", "generate_recommendation")
builder.add_edge("generate_recommendation", "format_report")
builder.add_edge("format_report", END)

stock_agent = builder.compile()