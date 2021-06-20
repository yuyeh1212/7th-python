import matplotlib.pyplot as plt

# X 軸
stock_list = ['2031', '2341', '2342', '2345']
# Y 軸
volumes = [34123, 122212, 41907, 3115987]

plt.bar(stock_list, volumes)

plt.plot(stock_list, volumes)

plt.pie(volumes, labels=stock_list)

plt.show()

plt.savefig('plot01.png')
