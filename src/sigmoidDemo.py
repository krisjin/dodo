import numpy as np
import matplotlib.pyplot as plt


# sigmoid

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)

y4 = sigmoid(x)

plt.plot(x, y4)
plt.ylim(-0.1, 1.1)
plt.show()
