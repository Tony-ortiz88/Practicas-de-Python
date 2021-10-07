import pandas as pd
from pandas_datareader import wb
from datetime import datetime
data = pd.read_csv("disney_prices.csv")
print(data.head())

from pandas_datareader.nasdaq_trader import get_nasdaq_symbols

symbols = get_nasdaq_symbols()
print(symbols)