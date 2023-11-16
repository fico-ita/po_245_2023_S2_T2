"""module to simulate a strategy."""
import numpy as np
import pandas as pd

from example.strategy_momentum import strategy_momentum


def momentum_simulator(path, data_source, t, ret_port, weights_db, **kwargs):
    r"""Calculate portfolio returns using your  strategy.

    Parameters:
        path (str): Path to save strategy data.
        strategy (function): The function representing your strategy.
        data_source (dict): Dictionary containing price data.
        t (int): Time value for calculation.
        ret_port (pd.Series): Accumulated portfolio returns.
        weights_db (pd.DataFrame): Accumulated weights database.
        **kwargs: Additional keyword arguments for the strategy function.

    Returns:
        pd.Series: Updated portfolio next day returns.
        pd.DataFrame: Updated weights database.

    Example:
        ```python
        import pandas as pd

        # Define MinRisk strategy function
        def min_risk_strategy(data_source, t, **kwargs):
            # Implementation of the MinRisk strategy
            # ...

        # Set parameters for strategy simulation
        path = "path/to/save/data/"
        t = 100  # Example time index
        ret_port = pd.Series(index=data_source['prices'].index)
        weights_db = pd.DataFrame()

        # Run strategy simulation
        ret_port, weights_db = strategy_simulator\\
            (path, min_risk_strategy, data_source, t, ret_port, weights_db)

        # Display the updated portfolio returns and weights database
        print(ret_port)
        print(weights_db)
        ```
    """
    # Calculate the weights for the specified time index (t)
    strategy = strategy_momentum
    weights = strategy(data_source, t=t, **kwargs)

    # Save weights to the weights database
    weights_db = pd.concat([weights_db, weights], axis=0)
    weights_db.to_parquet(path + "weights_db.parquet")

    # Calculate and save portfolio returns
    prices = data_source["prices"]
    prices_1 = prices[weights.ticker].loc[prices.index[t - 1 : t + 1]]
    returns_1 = np.log(prices_1).diff().tail(1).mean()
    weights_index = weights.weights
    weights_index.index = weights.ticker
    ret_port[prices.index[t]] = returns_1 @ weights_index

    aux = ret_port.reset_index()
    aux.columns = ["date", "ret_port"]
    aux.to_parquet(path + "ret_port.parquet")

    return ret_port, weights_db
