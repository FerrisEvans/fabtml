# 质地均匀的硬币
import random
import statistics
import matplotlib.pyplot as plt

# 实验的次数
num_flips = 1000

# 每次抛硬币的结果
res = []
# 每次抛硬币后的均值
running_means = []

for _ in range(num_flips):
    # 随机抛硬币，1代表正面（H），0代表反面（T）
    result_idx = random.randint(0, 1)
    res.append(result_idx)

    # 计算当前所有结果的均值
    mean_idx = statistics.mean(res)
    running_means.append(mean_idx)

# 可视化前 100 次结果均值随次数的变化
visual_num = 100
# 散点图
plt.scatter(range(1, visual_num + 1), res[0: visual_num], c=res[0: visual_num], marker='o', cmap="cool")
plt.plot(range(1, visual_num + 1), res[0: visual_num], c='r')
plt.xlabel('Number of coin flips')
plt.ylabel("Result")
plt.grid(True)
plt.show()

# 可视化均值随次数变化
plt.plot(range(1, num_flips + 1), running_means, c='b')
plt.axhline(0.5, color='r')
plt.xlabel('Number of coin flips')
plt.ylabel('Running Means')
plt.grid(True)
plt.ylim(0, 1)
plt.show()
