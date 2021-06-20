import matplotlib.pyplot as plt

# X 軸
stock_list = ['11/1', '11/2', '11/3', '11/4']
# Y 軸
prices = [23, 41, 41, 3]

plt.plot(stock_list, prices)
# 若使用 VS Code 搭配 terminal 終端機或 Jupyter Notebook 執行使用
plt.show()
# 若使用 repl.it 執行需要將圖表存為圖片後於左方資料夾選擇圖片檔案觀看結果
plt.savefig('plot.png')
