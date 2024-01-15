from statsmodels.tsa.stattools import adfuller
import pandas as pd
import matplotlib.pyplot as plt

def stationary_data(dataset):
    """
    Takes a dataset than check for all columns if they are stationary
    
    Parameters:
    - dataset: pd.dataFrame
    
    Returns:
    String that infomrs what columns are non stationary
    """

    # return values
    non_stationary_columns = []
    non_stationary_values = []

    # iterate over the df:
    for column_name, column_values in dataset.items():
        current_p = adfuller(column_values)[1]
        if current_p >= 0.05:
            non_stationary_columns.append(column_name)
            non_stationary_values.append(current_p)
    return non_stationary_columns, non_stationary_values

# load data
csv_file_path = './CORUMBA.csv'
corumba = pd.read_csv(csv_file_path, skiprows=1, header=0).iloc[:, 1:-1  ]
corumba = corumba.iloc[:-5, 1:-1]  #droping the first and last columns and last 5 lines
#print(corumba)
stationary_data = stationary_data(corumba)
print('Colunas não estacionárias: ' + str(stationary_data[0]))
print('Valores de p: ' + str(stationary_data[1]))