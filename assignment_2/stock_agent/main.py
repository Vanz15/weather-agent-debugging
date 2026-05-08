from graph import stock_agent


def main():
    ticker = input("Enter stock ticker symbol: ").strip()

    initial_state = {
        "ticker": ticker,
        "stock_data": None,
        "indicators": None,
        "recommendation": None,
        "report": None,
        "error": None,
    }

    try:
        final_state = stock_agent.invoke(initial_state)
        print(final_state["report"])

    except Exception as error:
        print("\nError:")
        print(error)


if __name__ == "__main__":
    main()