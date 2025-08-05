import numpy as np
import matplotlib.pyplot as plt

# 生成横轴数据
x_array = np.linspace(0, 2 * np.pi, 500)
# 正弦函数数据
sin_y = np.sin(x_array)
# 余弦函数数据
cos_y = np.cos(x_array)
# 设置图片大小
fig, ax = plt.subplots(figsize=(8, 6))
# 绘制正弦和余弦曲线
ax.plot(x_array, sin_y, label="sin(x)", color="blue", linewidth=2)
ax.plot(x_array, cos_y, label="cos(x)", color="red", linewidth=2)
# 设置标题、横轴和纵轴标签
ax.set_title("Sine and cosine functions")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
# 添加图例
ax.legend()
# 设置横轴和纵轴范围
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
# 设置横轴标签和刻度标签
x_ticks = np.arange(0, 2*np.pi+np.pi/2, np.pi/2)
x_ticklabels = [r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"]
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticklabels)
# 横纵轴采用相同的 scale
ax.set_aspect("equal")
ax.grid()
# 将图片保存为 SVG 格式
# plt.savefig("正余弦函数曲线.svg", format="svg")
plt.show()
