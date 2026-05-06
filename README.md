# Weather Agent Debugging

## Overview

This project is a repaired and fully functional LangGraph-based weather agent created for the AI/LLM Internship Assignment.

The agent detects the user’s location using an IP geolocation API, retrieves current weather information from the Open-Meteo API, and generates a readable weather report.

The assignment focused on identifying, debugging, and systematically fixing multiple issues across:
- LangGraph workflow execution
- state propagation
- API integration
- configuration management
- helper function logic
- output formatting
- testing and error handling

## Project Architecture

The application follows a sequential LangGraph workflow:

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

Each node updates and propagates shared state throughout the workflow.

## Features

- IP-based location detection
- Current weather retrieval using Open-Meteo
- Human-readable weather report generation
- Temperature classification
- Error handling for invalid API responses
- Mocked unit tests for deterministic testing
- LangGraph state-based workflow orchestration

## Technologies Used

- Python
- LangGraph
- LangChain
- Pydantic
- Requests
- unittest
- unittest.mock

## Installation

Clone the repository:

```bash
git clone https://github.com/Vanz15/weather-agent-debugging.git
cd weather-agent-debugging
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Weather Agent

Run the application:

```bash
python main.py
```

The application will prompt for the user’s name and generate a weather report.

## Running Tests

Execute the test suite:

```bash
python -m unittest test_weather_agent.py
```

The tests validate:
- daytime weather scenario
- nighttime weather scenario
- invalid location response handling

Mocked API responses are used to ensure deterministic and reliable testing.

## Debugging Summary

The following issues were identified and fixed during debugging:

| Issue | Resolution |
|---|---|
| Missing dependency installation | Installed required packages |
| Invalid Pydantic configuration field | Removed invalid placeholder field |
| Incorrect Python entry point | Fixed `__name__ == "__main__"` |
| Incorrect LangGraph execution flow | Added missing weather-fetching node |
| Missing state propagation | Saved location data into state |
| API field mismatch | Standardized `country_name` |
| Broken temperature classification logic | Replaced invalid truthy check |
| Incorrect variable interpolation | Fixed weather output formatting |
| External API rate limiting | Added mocked unit tests |

## Notebook Documentation

A complete debugging walkthrough is included in:

```text
Weather_Agent_Debugging.ipynb
```

The notebook documents:
- debugging approach
- root cause analysis
- fixes implemented
- testing strategy
- mocked execution examples
- final results

## Repository Structure

```text
weather-agent-debugging/
│
├── main.py
├── graph.py
├── requirements.txt
├── test_weather_agent.py
├── Weather_Agent_Debugging.ipynb
├── README.md
│
└── components/
    ├── __init__.py
    ├── config.py
    ├── helper_functions.py
    ├── nodes.py
    ├── schema.py
    └── state.py
```

## Final Result

The final implementation successfully:
- compiles and executes the LangGraph workflow
- propagates state correctly between nodes
- generates readable weather reports
- handles invalid API data safely
- passes all unit tests
- demonstrates reproducible debugging and testing practices