import numpy as np
import matplotlib.pyplot as plt


# 与门感知机
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


y1 = AND(3, 0)

print(y1)

#
# 导入权重和偏置

x = np.array([0, 1])  # 输入
w = np.array([0.5, 0.5])  # 权重

b = -0.7

y2 = np.sum(w * x) + b

print(y2)

## 使用权重和偏置实现与门

'''
偏置是调整神经元被激活的容易程度
'''


def AND2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])

    b = -0.7

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 仅权重值和偏置于AND不同

    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 仅权重值和偏置于AND不同

    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1


# 阶跃函数


def step_function(x):
    return np.array(x > 0, dtype=np.int)


def step_function2(x):
    y = x > 0
    return y.astype(np.int)


x = np.arange(-0.5, 5.0, 0.1)

y = step_function2(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # 指定y轴的范围

plt.show()


# sigmoid

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)

y4 = sigmoid(x)

plt.plot(x, y4)
plt.ylim(-0.1, 1.1)
plt.show()
