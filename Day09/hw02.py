import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

df = pd.read_csv('stock_data.csv')
data = df.loc[0:5, ['證券代號', '收盤價']]
data = data.set_index('證券代號')
print(data)
axes = data.plot(kind='line')

myfont = FontProperties(fname=r'NotoSansCJK-Black.ttc')
plt.title("個股日成交價", fontProperties=myfont)
plt.xlabel('證券代號', fontProperties=myfont)
plt.ylabel('收盤價', fontProperties=myfont)
plt.legend(prop=myfont)

for label in axes.get_xticklabels():
    label.set_fontproperties(myfont)
plt.show()
