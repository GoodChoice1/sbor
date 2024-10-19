# Вариант 123

# Размерность: 12 * 12
# Действия с числами: Поменять местами максимальный и минимальный элементы
# Действия с матрицей:  

import numpy as np

# Генерация случайной квадратной матрицы 12x12
matrix = np.random.randint(1, 100, (12, 12))
print(matrix)

# Находим индексы минимального и максимального элементов
min_idx = np.unravel_index(np.argmin(matrix), matrix.shape)
max_idx = np.unravel_index(np.argmax(matrix), matrix.shape)

# Преобразуем элементы и индексы в стандартный тип Python int для более читаемого вывода
min_element = int(matrix[min_idx])
max_element = int(matrix[max_idx])
min_idx = tuple(map(int, min_idx))
max_idx = tuple(map(int, max_idx))
print(f"Минимальный элемент: A{min_idx} = {min_element}")
print(f"Максимальный элемент: A{max_idx} = {max_element}")

# Меняем местами минимальный и максимальный элементы
matrix[min_idx], matrix[max_idx] = matrix[max_idx], matrix[min_idx]

print("\nМатрица после замены минимального и максимального элементов:")
print(matrix)

# Вычисляем обратную матрицу matrix^-1
matrix_inverted = np.linalg.inv(matrix)
np.set_printoptions(precision=4, suppress=True)
print("\nОбратная матрица matrix^-1:")
print(matrix_inverted)
