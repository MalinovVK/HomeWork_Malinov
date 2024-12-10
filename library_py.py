import matplotlib.pyplot as plt
import numpy as np

fig, axe = plt.subplots()
x = np.array([5, 8, 14, 20, 25])
y = np.array([5, 5, 7, 9, 12])
axe.plot(x, y, color='green', linestyle='-', marker='o', label='1')
axe.plot(2 * x, y, color='red', linestyle='-', marker='o', label='2')
axe.set_title('Заголовок графика', fontsize=15)
axe.legend(loc = 'lower left')
plt.plot(x, y)
plt.show()
