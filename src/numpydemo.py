import numpy as np

x = np.array([1, 2, 3, 4, 5])

print(x)

print(type(x))

y = np.array([1, 2, 3, 4, 5])

z = x + y

print(z / 2.0)

## 多维数组


w = np.array([[1, 2], [3, 4]])
v = np.array([[3, 0], [0, 6]])

print(w)
print(w.shape)
print(w.dtype)

print(w + v)

# 单一标量运算
print(w * 10)

# 广播

print("######################################")
c = np.array([10, 20])

print(w * c)

# 访问元素
print("#####################################")
w[0]  # 访问第一行

w[0][1]

for row in w:
    print(row)

# 转换为一位数组
w = w.flatten()
print(w > 15) #抽取大雨15的元素
