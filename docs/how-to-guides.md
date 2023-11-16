## How can  simulate and study the momentum strategy?
If you have a dataset and need to simulate momentum strategy, you're in luck! The momentum package can assist you in accomplishing this. Download the code from this GitHub repository and put the momentum folder in the same directory as yours.

    your_project/
    │
    ├── modules/
    │   ├── __init__.py
    │   └── get_retornos.py
    │   └── initial_weights.py
    │   └── load_data.py
    │   └── strategy_simulator.py
    │   
    ├── example/
    │   ├── __init__.py
    │   └── strategy_momentum.py    
    │
    ├── dataset/
    │   ├── BR/
    │   └── US/   
    │
    └── your_notebook.ipynb
!!! warning
    Ensure that you upload your dataset for simulation. Alternatively, you can use the dataset in the actual repository. If you choose to add your own dataset, please adhere to the same file format standardization as the files present in the repository's dataset.

Within your notebook, you can import the `momentum` function from the `momentum.strategy_momentum` module using the following code:

    # your_notebook.ipynb
    from momentum.strategy_momentum import momentum

After importing the function into your notebook, you can use the modules along with the chosen dataset to simulate the momentum strategy with various parameters of your choice.
