import random
import statistics
import matplotlib.pyplot as plt

random.seed(0) # 方便复刻结果
mean1, std1, size1 = 0, 1, 300 # 均值、标准差、样本数量
data1 = [random.gauss(mean1, std1) for _ in range(size1)]
mean2, std2, size2 = 10, 5, 700
data2 = [random.gauss(mean2, std2) for _ in range(size2)]
# 混合
mixed_data = data1 + data2
mean_loc = statistics.mean(mixed_data)
std_loc = statistics.stdev(mixed_data)

# 直方图
plt.hist(mixed_data, bins=30, density=True, edgecolor='black', alpha=0.75, color='red', label="Mixed data")
plt.axvline(mean_loc, color='red', linestyle='--', label="Mean")
plt.axvline(mean_loc + std_loc, color='blue', linestyle='--', label="Mean +- std")
plt.axvline(mean_loc - std_loc, color='blue', linestyle='--')
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.title("Histogram of Mixed data")
plt.grid(True)
plt.show()
