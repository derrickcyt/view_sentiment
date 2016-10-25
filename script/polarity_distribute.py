# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

result = defaultdict(int)

in_f = open("../experiment/simple_match/result/result.csv", "r")
in_f.readline()
for line in in_f:
    arr = line.strip().split(",")
    polarity = arr[2]
    result[polarity] += 1
in_f.close()

width = 2
ind = np.linspace(0.5, 9.5, 3)

fig = plt.figure(1)

print result
plt.bar(ind - width / 2, result.values(), width, color="blue")

plt.xticks(ind, result.keys())
plt.show()
