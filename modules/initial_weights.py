"""Module to generate initial weights."""

import random

import numpy as np


def get_uniform_noneg(size):
    """Generate initial uniform weights (non-negative).

    Parameters:
        size (int): Number of weights to generate.

    Returns:
        ndarray: Array of initial uniform weights.

    Example:
        ```python
        import numpy as np

        # Set the size of weights
        size = 10  # Example size

        # Generate initial uniform weights (non-negative)
        initial_weights_noneg = get_uniform_noneg(size)

        # Display the generated initial weights
        print(initial_weights_noneg)
        ```
    """
    aux = [random.uniform(0, 2 / size) for _ in range(size)]

    return np.array(aux)  # Start with all weights set to 0


# Generate Initial Uniform Weights (Positive and Negative)


def get_uniform_posneg(size):
    """Generate initial uniform weights (positive and negative).

    Parameters:
        size (int): Number of weights to generate.

    Returns:
        ndarray: Array of initial uniform weights.

    Example:
        ```python
        import numpy as np

        # Set the size of weights
        size = 10  # Example size

        # Generate initial uniform weights (positive and negative)
        initial_weights_posneg = get_uniform_posneg(size)

        # Display the generated initial weights
        print(initial_weights_posneg)
        ```
    """
    aux = [random.uniform(-2 / size, 2 / size) for _ in range(size)]

    return np.array(aux)  # Start with all weights set to 0
