# 头重脚轻的硬币
import random
import statistics

num_flips = 1000

res = [random.choices([0, 1], [0.4, 0.6])[0] for _ in range(num_flips)]
running_means = [statistics.mean(res[0: idx + 1]) for idx in range(num_flips)]
