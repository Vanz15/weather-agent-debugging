# LangGraph Assessment

## Overview

This repository contains two LangGraph-based assignments completed as part of an AI/LLM Internship Assessment.

The assignments focus on:
- debugging and repairing an existing LangGraph workflow
- designing and implementing a LangGraph agent from scratch
- modular workflow architecture
- state propagation
- testing and reproducibility
- error handling and documentation

---

# Repository Structure

```text
langgraph-assessment/
├── .gitignore
├── README.md
│
├── assignment_1/
│   ├── weather_agent_debug.ipynb
│   └── weather_agent/
│       ├── main.py
│       ├── graph.py
│       ├── requirements.txt
│       ├── test_weather_agent.py
│       └── components/
│
└── assignment_2/
    ├── stock_analysis_demo.ipynb
    └── stock_agent/
        ├── main.py
        ├── graph.py
        ├── requirements.txt
        ├── test_stock_agent.py
        └── components/
```

---

# Assignment 1 — Weather Agent Debugging

## Objective

The first assignment focused on debugging and repairing a broken LangGraph-based weather agent.

The application:
- detects user location using IP geolocation
- retrieves weather data
- generates a formatted weather report

The assignment emphasized:
- systematic debugging
- identifying workflow issues
- fixing state propagation bugs
- handling API failures
- documenting the debugging process

---

## Assignment 1 Features

- IP-based location detection
- weather retrieval from external APIs
- formatted weather reports
- temperature classification
- LangGraph state-based workflow
- mocked testing
- robust error handling

---

## Assignment 1 Workflow

```text
START
  ↓
fetch_location_data
  ↓
fetch_weather_data
  ↓
generate_weather_info
  ↓
END
```

---

## Assignment 1 Debugging Highlights

The following issues were identified and fixed:
- missing dependency installation
- incorrect LangGraph execution flow
- graph compilation issues
- invalid Pydantic field definitions
- broken temperature classification logic
- state propagation bugs
- incorrect API field handling
- formatting inconsistencies
- API rate-limiting handling

---

## Assignment 1 Notebook

The debugging walkthrough is documented in:

```text
assignment_1/weather_agent_debug.ipynb
```

The notebook includes:
- debugging approach
- root cause analysis
- implemented fixes
- testing strategy
- working demonstrations
- error handling validation

---

## Running Assignment 1

Navigate to the project:

```bash
cd assignment_1/weather_agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Run tests:

```bash
python -m unittest test_weather_agent.py
```

---

# Assignment 2 — Stock Market Analysis Agent

## Objective

The second assignment focused on building a LangGraph-based stock market analysis agent from scratch.

The application:
- accepts stock ticker symbols
- retrieves historical stock data using `yfinance`
- calculates technical indicators
- generates BUY/HOLD/SELL recommendations
- formats financial analysis reports

The assignment emphasized:
- workflow architecture design
- technical indicator implementation
- modular engineering
- reproducible testing
- graceful error handling

---

## Assignment 2 Features

- stock ticker validation
- historical stock data retrieval
- 10-day Simple Moving Average
- 20-day Simple Moving Average
- 14-day Relative Strength Index (RSI)
- BUY/HOLD/SELL recommendation logic
- formatted analysis reports
- mocked testing
- deterministic execution

---

## Assignment 2 Workflow

```text
START
  ↓
validate_ticker
  ↓
fetch_stock_data
  ↓
calculate_indicators
  ↓
generate_recommendation
  ↓
format_report
  ↓
END
```

---

## Recommendation Logic

### BUY

```text
current price > SMA 10 > SMA 20
and RSI < 70
```

### SELL

```text
current price < SMA 10 < SMA 20
and RSI > 30
```

### HOLD

If neither BUY nor SELL conditions are satisfied, the agent recommends HOLD.

---

## Assignment 2 Notebook

The implementation walkthrough is documented in:

```text
assignment_2/stock_analysis_demo.ipynb
```

The notebook includes:
- architecture explanation
- technical indicator discussion
- live demonstrations
- mocked demonstrations
- error handling examples
- testing workflow

---

## Running Assignment 2

Navigate to the project:

```bash
cd assignment_2/stock_agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Run tests:

```bash
python -m unittest test_stock_agent.py
```

---

# Technologies Used

- Python
- LangGraph
- LangChain
- Pydantic
- Requests
- yfinance
- pandas
- numpy
- unittest
- unittest.mock

---

# Environment Setup

Create and activate a virtual environment.

## Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

Dependencies for each assignment are installed separately using their respective `requirements.txt` files.

---

# Testing

Both assignments include unit tests.

The tests validate:
- workflow execution
- state propagation
- indicator calculations
- report generation
- error handling
- mocked API responses

Mocked data is used where appropriate to ensure deterministic and reproducible execution.

---

# Final Result

The completed repository demonstrates:
- debugging existing LangGraph systems
- building LangGraph agents from scratch
- state-based workflow orchestration
- modular software engineering practices
- deterministic testing
- reproducible project structure
- robust error handling
- clear technical documentation