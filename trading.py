#c:/Users/Rosary/Desktop/trading/.venv/Scripts/activate.bat
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import datetime as dt
from scipy import stats
import csv
import yfinance as yf

stockdata = yf.download('KTB.BK', start='2013-01-01', end='2023-12-18')
stockdataDesc = stockdata.sort_values(by='Date', ascending=False)
stockdata.head()
stockdata['Return'] = stockdata['Close'].pct_change()
stockdata = stockdata.dropna()
stockdata['CumReturn'] = (1 + stockdata['Return']).cumprod() - 1
stockdata['Mean'] = stockdata['Return'].mean()
stockdata['variance'] = stockdata['Return'].var()
stockdata['Skewness'] = stockdata['Return'].skew()
stockdata['Kurtosis'] = stockdata['Return'].kurtosis()

stockdata['Real_Kurtosis'] = stockdata['Kurtosis'] + 3
print(stockdata)

header = ['date', 'high', 'low', 'open', 'close', 'volume', 'Adj Close', 'Return', 'CumReturn', 'Mean', 'variance', 'Skewness', 'Kurtosis', 'Real_Kurtosis']

with open('stockdata.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(stockdata.reset_index().values)
