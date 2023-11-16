"""Module to calculate returns of stocks at a specific time."""

import numpy as np

# Calculate Returns of S&P 500 Stocks at a Specific Time


def get_retornos_sp(data, t, window_size):
    """Calculate the returns of S&P 500 stocks at a specific time.

    Parameters:
        data (dict): Data dictionary containing 'sp' and 'prices' DataFrames.
        t (int): The desired time.
        window_size (int): Size of the window for calculations.

    Returns:
        DataFrame: Calculated returns based on the input data.

    Example:
        ```python
        import pandas as pd

        # Load financial data for testing
        data = load_data_US()

        # Set parameters for calculating returns
        t = 100  # Example time index
        window_size = 252  # Example window size

        # Calculate returns for S&P 500 stocks at the specific time
        returns_sp = get_retornos_sp(data, t, window_size)

        # Display the calculated returns
        print(returns_sp)
        ```
    """
    sp500 = data["sp"]
    prices = data["prices"]
    dates_prices = prices.index

    local_sp500 = dates_prices[t] > sp500["Date"]

    data_sp500 = sp500["Date"][local_sp500].tail(1).values[0]
    # data_sp500 = sp500["Date"].to_numpy()[local_sp500].tail(1)[0] correção sugerida no rufus

    sp500_t = sp500["Ticker"].loc[sp500["Date"] == data_sp500]
    prices_t = prices[sp500_t].loc[dates_prices[t - window_size : t]].dropna(axis=1)

    return np.log(prices_t).diff().fillna(0)


# Calculate Returns of IBOV Stocks at a Specific Time


def get_retornos_ibov(data, t, window_size):
    """Calculate the returns of IBOV stocks at a specific time.

    Parameters:
        data (dict): Data dictionary containing 'IBOV' and 'prices' DataFrames.
        t (int): The desired time.
        window_size (int): Size of the window for calculations.

    Returns:
        DataFrame: Calculated returns based on the input data.

    Example:
        ```python
        import pandas as pd

        # Load financial data for testing
        data = load_data_BR()

        # Set parameters for calculating returns
        t = 100  # Example time index
        window_size = 252  # Example window size

        # Calculate returns for IBOV stocks at the specific time
        returns_ibov = get_retornos_ibov(data, t, window_size)

        # Display the calculated returns
        print(returns_ibov)
        ```
    """
    ibov = data["ibov"]
    prices = data["prices"]
    dates_prices = prices.index

    local_ibov = dates_prices[t] > ibov["Date"]
    data_ibov = ibov["Date"][local_ibov].tail(1).values[0]
    #data_ibov = ibov["Date"].to_numpy()[local_ibov].tail(1)[0] correção sugerida no rufus

    ibov_t = ibov["Ticker"].loc[ibov["Date"] == data_ibov]
    prices_t = prices[ibov_t].loc[dates_prices[t - window_size : t]]

    return np.log(prices_t).diff().fillna(0)
