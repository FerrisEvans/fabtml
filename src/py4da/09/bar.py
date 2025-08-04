import matplotlib.pyplot as plt

# 创建图表，设置大小
plt.figure(figsize=(12, 8))
# 柱状图
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 80, 130, 120]

plt.bar(month, sales, color='orange')

plt.show()
