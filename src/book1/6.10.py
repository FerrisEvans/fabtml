import math
import matplotlib.pyplot as plt

x_start = 0 # 弧度值
print(math.sin(x_start))
x_end = 2 * math.pi
print(math.sin(x_end))

# 等差数列
num = 37
# 公差
step = (x_end - x_start) / (num - 1)
# 生成等差数列
x_array = [x_start + i * step for i in range(num)]
zero_array = [0 for i in range(num)]

# 可视化
plt.plot(x_array, zero_array, marker='.', markersize=5, markeredgecolor='r', markerfacecolor='g')
plt.text(x_start, 0, '0')
plt.text(x_end, 0, r'$2\pi$')
plt.axis('off')
plt.show()

y_array = [math.sin(x_idx) for x_idx in x_array]
plt.plot(x_array, y_array, marker='.', markersize=5, markeredgecolor='r', markerfacecolor='g')
plt.text(x_start, -0.1, '0')
plt.text(x_end, 0.1, r'$2\pi$')
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.25)
plt.axis('off')
plt.show()
