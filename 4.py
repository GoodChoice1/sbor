# Вариант 6479

# Гипотеза: Гипотеза о равенстве математических ожиданий при известных дисперсиях
# Выборка 1: N(10,2)
# Выборка 2: N(5,2)
# a: 0.3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, ttest_ind

def plot_distribution(mean1, std1, mean2, std2, sample_size):
    # Генерация двух выборок
    sample1 = np.random.normal(mean1, std1, sample_size)
    sample2 = np.random.normal(mean2, std2, sample_size)
    
    # Построение экспериментальных плотностей
    plt.figure(figsize=(10,6))
    plt.hist(sample1, bins=30, density=True, alpha=0.6, color='blue', label="Выборка 1 (N(10, 2))")
    plt.hist(sample2, bins=30, density=True, alpha=0.6, color='red', label="Выборка 2 (N(5, 2))")
    
    # Теоретические плотности
    x = np.linspace(min(sample1.min(), sample2.min()) - 1, max(sample1.max(), sample2.max()) + 1, 100)
    plt.plot(x, norm.pdf(x, mean1, std1), 'b-', lw=2, label='Теоретическая N(10, 2)')
    plt.plot(x, norm.pdf(x, mean2, std2), 'r-', lw=2, label='Теоретическая N(5, 2)')
    
    plt.title('Экспериментальные и теоретические функции плотности')
    plt.legend()
    plt.xlabel('Значение')
    plt.ylabel('Плотность')
    plt.show()

# Проверка гипотезы о равенстве средних при известных дисперсиях
def test_hypothesis(sample1, sample2, alpha):
    # t-test для независимых выборок
    t_stat, p_value = ttest_ind(sample1, sample2)
    print(f"t-значение: {t_stat:.4f}, p-значение: {p_value:.4f}")
    
    # Проверка гипотезы
    if p_value < alpha:
        print(f"Отвергаем нулевую гипотезу на уровне значимости {alpha}")
    else:
        print(f"Не отвергаем нулевую гипотезу на уровне значимости {alpha}")

# Параметры
mean1, std1 = 10, 2
mean2, std2 = 5, 2
sample_size = 100
alpha = 0.3

# Генерация и тест
sample1 = np.random.normal(mean1, std1, sample_size)
sample2 = np.random.normal(mean2, std2, sample_size)

# Построение графиков
plot_distribution(mean1, std1, mean2, std2, sample_size)

# Проверка гипотезы
test_hypothesis(sample1, sample2, alpha)
