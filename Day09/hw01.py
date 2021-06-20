import pandas as pd

df = pd.read_csv('stock_data.csv')
data = df.loc[1:6, ['證券代號', '證券名稱', '收盤價', '成交筆數']]
data = data.set_index('證券代號')
print(data)
