from statsmodels.tsa.stattools import adfuller
from numpy import log
import pandas as pd

csv_file_path = './CORUMBA.csv'
corumba = pd.read_csv(csv_file_path, skiprows=1, header=0)
#print(corumba)

adf_test = adfuller(corumba['JAN'])
print('ADF Statistic: %f' % adf_test[0])
print('p-value: %f' % adf_test[1])