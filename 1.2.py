# Вариант 323

# Вид распределения: Гамма
# Мат ожидание: 2; Дисперсия: 10
# Параметр массива: Максимальный элемент

import numpy as np
import matplotlib.pyplot as plt

mean = 2  # Математическое ожидание
variance = 10  # Дисперсия

# Параметры распределения Gamma
beta = mean / variance # = 1/scale
alpha = mean * beta

amount = 20

# Генерация массива из 20 элементов, распределенных по закону Гамма
data = np.random.gamma(alpha, 1/beta, amount)
print(f"Массив: ${data}")

max_element = np.max(data)
print(f"Максимальный элемент: {max_element}")

plt.figure()
plt.hist(data, bins=10)
plt.title("Гамма распределение")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

plt.figure()
plt.boxplot(data)
plt.title("Boxplot")
plt.grid(True)
plt.show()
