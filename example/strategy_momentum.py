"""Module that contains the implementation of the momentum strategy.."""

import pandas as pd

from modules.get_retornos import get_retornos_ibov, get_retornos_sp


def strategy_momentum(data, t, size=10, window_size=500, momentum_window=252):
    r"""Implement a Momentum-based strategy with equal weights for selected stocks.

    Parameters:
        data (dict): Data dictionary containing market and 'prices' DataFrames.
        t (int): The desired time.
        size (int, optional): Number of stocks to consider. Defaults to 10.
        window_size (int, optional): \\
            Size of the window for calculations. Defaults to 500.
        momentum_window (int, optional): \\
            Window size for calculating Momentum. Defaults to 252.

    Returns:
        DataFrame: Equal weights for the selected top Momentum stocks.

    Example:
        ```python
        import pandas as pd

        # Load financial data for testing
        data = load_data_BR()

        # Set parameters for the strategy
        t = 100  # Example time index
        size = 5  # Example: Select top 5 stocks
        window_size = 500
        momentum_window = 252

        # Apply the momentum-based strategy
        optimal_weights = strategy_momentum \\
                        (data, t, market, size, window_size, momentum_window)

        # Display the optimal weights
        print(optimal_weights)
        ```
    """
    market = 1
    # Calculate Momentum
    if market == 0:
        returns = get_retornos_sp(data, t, window_size)
    elif market == 1:
        returns = get_retornos_ibov(data, t, window_size)

    momentum = returns.rolling(window=momentum_window).mean().iloc[-1]

    # Select top 'size' stocks with the highest Momentum
    top_momentum_stocks = momentum.nlargest(size).index.tolist()

    # Calculate equal weights
    weight_per_stock = 1.0 / size
    weights = [weight_per_stock] * size

    return pd.DataFrame(
        {
            "date": [data["prices"].index[t]] * len(top_momentum_stocks),
            "ticker": top_momentum_stocks,
            "weights": weights,
        },
    )
