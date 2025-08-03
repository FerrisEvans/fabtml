import matplotlib.pyplot as plt

# 创建图表，设置大小
plt.figure(figsize=(12, 8))
# 折线图
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 80, 130, 120]

plt.plot(month, sales)
plt.xticks(month, month)
plt.title('Sales by Month', color='red', fontsize=26)
# 坐标轴标签
plt.xlabel('Month', color='red')
plt.ylabel('Sales', color='red')
# 图例
plt.legend(['Product'], loc='upper left')
# 网格线
# plt.grid(axis='x')
# plt.grid(axis='y')
plt.grid(True, alpha=0.5, linestyle='--', color='blue', marker='o')
# 设置刻度字体大小
plt.xticks(rotation=60, fontsize=20)
# 设置 y 轴范围
plt.ylim(0, 160)
# 在每个数据点上显示数值
for x, y in zip(month, sales):
    plt.text(x, y, str(y), ha='center', va='bottom')
plt.show()
