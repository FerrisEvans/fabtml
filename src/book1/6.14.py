import random
import statistics
import matplotlib.pyplot as plt

num = 50
random.seed(0)
x_data = [random.uniform(0, 10) for _ in range(num)]
# 噪声
noise = [random.gauss(0, 1) for _ in range(num)]
y_data = [0.5 * x_data[idx] + 1 + noise[idx] for idx in range(num)]

# 散点图
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0, 10)
ax.set_ylim(-2, 8)
ax.grid()

# 一元线性回归
slope, intercept = statistics.linear_regression(x_data, y_data)

# 等差数列
start, end, step = 0, 10, 0.5
x_array = []
x_i = start

while x_i <= end:
    x_array.append(x_i)
    x_i += step

# 计算 x_array 的预测值
y_array_predicted = [slope * x_i + intercept for x_i in x_array]

# 可视化一元线性回归直线
fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.plot(x_array, y_array_predicted, color='red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0, 10)
ax.set_ylim(-2, 8)
ax.grid()
plt.show()
