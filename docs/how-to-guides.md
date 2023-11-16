## Como simular e estudar a estrategia de momentum?
Se voce tem um dataset e precisa simular a estrategia de momentum, voce esta com sorte! 
O pacote `momentum` pode te ajudar a fazer isso.
Download the code from this GitHub repository and place
the `momentum` folder in the same directory as your

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
