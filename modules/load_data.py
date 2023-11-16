"""Load financial data for US and Brazil."""
import pandas as pd


def load_data_us():
    """Load financial data for US analysis.

    Returns:
        dict: A dictionary containing the following DataFrames:
        - 'rate': DataFrame with Federal Reserve rates.
        - 'sp': DataFrame with S&P 500 components.
        - 'prices': DataFrame with historical stock prices for S&P 500 companies.

    Example:
        ```python
        import pandas as pd

        # Load financial data for US analysis
        data_us = load_data_US()

        # Display the loaded data
        print(data_us)
        ```
    """
    # Load Federal Reserve rates
    rate = pd.read_parquet("dataset/US/fed_rate.parquet")

    # Load S&P 500 components
    sp = pd.read_parquet("dataset/US/sp_comp.parquet")

    # Load historical stock prices for S&P 500 companies
    melt_prices = pd.read_parquet("dataset/US/prices_sp.parquet")
    df_prices = melt_prices.pivot_table(index="Date", columns="Ticker", values="value")

    # Create a dictionary with data

    return {"rate": rate, "sp": sp, "prices": df_prices}


# Load Financial Data for Brazil


def load_data_br():
    """Load financial data for Brazil.

    Returns:
        dict: A dictionary containing the following DataFrames:
        - 'rate': DataFrame with Selic rates.
        - 'ibov': DataFrame with Ibovespa components.
        - 'prices': DataFrame with historical stock prices for Ibovespa companies.

    Example:
        ```python
        import pandas as pd

        # Load financial data for Brazil
        data_br = load_data_BR()

        # Display the loaded data
        print(data_br)
        ```
    """
    # Load Selic rates and format for the same pattern as the Fed rate
    rate = pd.read_parquet("dataset/BR/selic.parquet")
    rate = rate.drop(columns=["anula100"])
    rate = rate.rename(columns={"data": "date", "diario": "daily_rate"})
    rate["date"] = pd.to_datetime(rate["date"], format="%d/%m/%Y")

    # Load Ibovespa components and format for the same pattern as S&P 500
    ibov = pd.read_parquet("dataset/BR/ibov_comp.parquet")
    ibov = ibov.reset_index(drop=True)
    ibov = ibov.drop(columns=["participacao"])
    ibov = ibov.rename(columns={"date": "Date", "ticker": "Ticker"})
    ibov["Date"] = pd.to_datetime(ibov["Date"])

    # Load historical stock prices for Ibovespa companies
    melt_prices = pd.read_parquet("dataset/BR/prices_ibov.parquet")
    melt_prices.index.names = ["Date"]
    melt_prices.index = pd.to_datetime(melt_prices.index, format="%d/%m/%Y").strftime(
        "%Y-%m-%d",
    )
    melt_prices.index = pd.to_datetime(melt_prices.index)

    # Create a dictionary with loaded data
    dict_data = {"rate": rate, "ibov": ibov, "prices": melt_prices}

    # Additional Data Formatting
    dict_data["prices"].keys().name = "Ticker"
    dict_data["rate"]["daily_rate"] = dict_data["rate"]["daily_rate"].astype(float)
    dict_data["ibov"] = dict_data["ibov"][dict_data["ibov"].columns[::-1]]

    return dict_data
