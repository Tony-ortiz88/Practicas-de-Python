import codecademylib3_seaborn
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime
import pandas_datareader.wb as wb
import numpy as np

gold_prices = pd.read_csv('gold_prices.csv')
crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
print(gold_prices.head())


start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)
sap_data  = web.DataReader('SP500', 'fred', start, end)
print(sap_data.head())

nasdaq_data = web.DataReader('NASDAQ100', 'fred', start, end)

gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start=start, end=end)

export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start=start, end=end)

def log_return(prices):
  return np.log(prices / prices.shift(1))


gold_returns = log_return(gold_prices.Gold_Price)
crudeoil_returns = log_return(crude_oil_prices.Crude_Oil_Price)
sap_returns = log_return(sap_data['SP500'])
gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])




print (gold_returns.head())
print (crudeoil_returns.head())
print (sap_returns.head())
print (gdp_returns.head())

print('gold:', gold_returns.var())
print('oil:', crudeoil_returns.var())
print('sap:', sap_returns.var())
print('gdp:', gdp_returns.var())








