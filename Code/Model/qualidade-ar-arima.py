import numpy as np
import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt

import pmdarima as pm

def parser(s):
    return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

df = pd.read_csv('../../data/raw/qualidade-ar-curitiba-2020.csv',parse_dates=['local_datetime'],date_parser=parser,index_col='local_datetime')

#df.shape

#df.head(2)

#df.plot()
#plt.show()

model = pm.auto_arima(df, seasonal=True, m=120)


forecasts = model.predict(n_periods=24) 


x = np.arange(1422)
#plt.plot(x[:1398], df, c='blue')
plt.plot(x[1398:], forecasts, c='green')
#plt.savefig('arima.png')
plt.show()
