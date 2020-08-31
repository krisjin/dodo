import numpy as np

import matplotlib.pyplot as plt
from matplotlib.image import imread

# 生成数据，以0.1为单位，生成0到6的数据
x = np.arange(0, 19, 1)
y1 = np.sin(x)  # sin函数

print(x)

y2 = np.cos(x)
# 绘制图形
plt.plot(x, [0.394894,0.409681,0.401056,0.405406,0.398342,0.405719,0.415794,0.400387,0.396646,0.401527,0.403123,0.431539,0.401495,0.401527,0.400940,0.398649,0.405719,0.400384,0.408686], label="train.error")

plt.plot(x, [0.403338,0.421645,0.400346,0.410318,0.403241,0.403879,0.425851,0.404255,0.400011,0.402663,0.406895,0.459267,0.402585,0.402663,0.394689,0.406577,0.403879,0.404311,0.418255], linestyle="--", label="validate.error")
plt.xlabel("epoch")
plt.ylabel("error")

plt.title("train.error&validate.error")
plt.legend()

plt.show()