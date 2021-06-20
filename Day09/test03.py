import pandas as pd

df = pd.read_csv('youbike_data.csv', encoding='utf-8')

print(df.info())
print(df.describe())
print(df[df['sarea'] == '三重區'])
