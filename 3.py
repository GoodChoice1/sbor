# Вариант 835

# Вид распределения 1: Рэлея
# Вид распределения 2: Эрланга
# Размер выборки: 90

import numpy as np
import matplotlib.pyplot as plt

n_samples = 90  # Размер выборки
n_experiments = 10000  # Количество экспериментов для проверки ЦПТ
erlang_shape = 2  # Параметр формы для распределения Эрланга

rayleigh_samples = np.random.rayleigh(scale=1, size=n_samples)
erlang_samples = np.random.gamma(erlang_shape, 1, n_samples)

def plot_histogram(data, title, bins_list):
    plt.figure(figsize=(18, 5))
    for i, bins in enumerate(bins_list):
        plt.subplot(1, len(bins_list), i+1)
        plt.hist(data, bins=bins)
        plt.title(f'{title} (интервалы={bins})')
        plt.xlabel('Значения')
        plt.ylabel('Частота')
    plt.show()

bins_list = [5, 10, n_samples]

plot_histogram(rayleigh_samples, 'Распределение Рэлея', bins_list)
plot_histogram(erlang_samples, 'Распределение Эрланга', bins_list)

# Проверка центральной предельной теоремы
def check_central_limit_theorem(distribution_fn, label, n_samples, n_experiments):
    means = [np.mean(distribution_fn(n_samples)) for _ in range(n_experiments)]
    
    plt.figure(figsize=(10, 5))
    plt.hist(means, bins=50, density=True)
    plt.title(f'Распределение средних значений по {n_experiments} выборкам ({label})')
    plt.xlabel('Средние значения')
    plt.ylabel('Частота')
    plt.show()

# Проверка для распределения Рэлея и Эрланга
check_central_limit_theorem(lambda size: np.random.rayleigh(scale=1, size=size), 'Распределение Рэлея', n_samples, n_experiments)
check_central_limit_theorem(lambda size: np.random.gamma(erlang_shape, 1, size), 'Распределение Эрланга', n_samples, n_experiments)
