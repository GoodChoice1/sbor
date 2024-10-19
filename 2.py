# Вариант 449

# Формат 1 -> Формат 2: CSV -> JSON
# Преобразование : Для каждой записи указать количество адресов
# Закон распределения для даты рождения : Экспоненциальное распределение

import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import csv
import json
import matplotlib.pyplot as plt

first_names = [
    "Aleksandr", "Dmitriy", "Maxim", "Artem", "Sergey", 
    "Andrey", "Aleksey", "Ivan", "Mikhail", "Nikita",
    "Olga", "Anna", "Elena", "Tatiana", "Maria",
    "Natalia", "Ekaterina", "Irina", "Vera", "Sofia"
]

last_names = [
    "Ivanov", "Smirnov", "Kuznetsov", "Popov", "Vasiliev", 
    "Petrov", "Sokolov", "Mikhailov", "Novikov", "Fedorov",
    "Morozov", "Volkov", "Alekseev", "Lebedev", "Semenov", 
    "Egorov", "Pavlov", "Kozlov", "Stepanov", "Nikolaev"
]

cities = [
    'Moskva', 'Sankt-Peterburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan', 
    'Nizhniy Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-na-Donu'
]

streets = [
    'Lenina', 'Kirova', 'Mira', 'Pobedy', 'Gagarina', 
    'Pushkina', 'Sovetskaya', 'Moskovskaya', 'Krasnaya', 'Zhukova'
]

def generate_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return first_name, last_name

def generate_gender():
    return random.choice(['Male', 'Female'])

# Генерация даты рождения с использованием экспоненциального распределения
def generate_birthdate():
    scale = 365 * 30  # Среднее значение возраста около 30 лет (в днях)
    random_days = int(np.random.exponential(scale))  # Генерация числа дней назад
    birthdate = datetime.now() - timedelta(days=random_days)  # Вычитаем из текущей даты
    return birthdate

def generate_address():
    city = random.choice(cities)
    street = random.choice(streets)
    house = random.randint(1, 200)
    apartment = random.randint(1, 500)
    return [city, street, house, apartment]

def generate_addresses():
    num_addresses = random.randint(1, 3)
    return [generate_address() for _ in range(num_addresses)]

data = []
for _ in range(1000):
    first_name, last_name = generate_name()
    birthdate = generate_birthdate()
    gender = generate_gender()
    has_driver_license = random.choice([True, False])
    addresses = generate_addresses()
    num_addresses = len(addresses)

    data.append({
        "first_name": first_name,
        "last_name": last_name,
        "birthdate": birthdate.strftime('%Y-%m-%d'),  # Сохраняем дату как строку в формате YYYY-MM-DD
        "gender": gender,
        "driver_license": has_driver_license,
        "addresses": addresses,
    })

csv_file = "data.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['First_Name', 'Last_Name', 'Birthdate', 'Gender', 'Driver_License', 'Addresses'])
    for record in data:
        writer.writerow([
            record['first_name'], 
            record['last_name'], 
            record['birthdate'], 
            record['gender'], 
            record['driver_license'], 
            record['addresses'],
        ])

df = pd.read_csv(csv_file, encoding='utf-8')

# Преобразование даты рождения в формат datetime
df['Birthdate'] = pd.to_datetime(df['Birthdate'])

plt.figure(figsize=(10, 6))
plt.hist(df['Birthdate'], bins=30)
plt.title("Гистограмма по дате рождения (данные из CSV)")
plt.xlabel("Дата рождения")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

# Перед сохранением в JSON добавляем количество адресов
df['Num_Addresses'] = df['Addresses'].apply(lambda x: len(eval(x)))  # Подсчет количества адресов

json_file = "filtered_data.json"
df.to_json(json_file, orient='records', date_format='iso', lines=True)

print("Данные с количеством адресов сохранены в файл JSON.")

json_df = pd.read_json(json_file, lines=True)

# Преобразование даты рождения в формат datetime после чтения из JSON
json_df['Birthdate'] = pd.to_datetime(json_df['Birthdate'], errors='coerce')

plt.figure(figsize=(10, 6))
plt.hist(json_df['Birthdate'], bins=30)
plt.title("Гистограмма по дате рождения (данные из JSON)")
plt.xlabel("Дата рождения")
plt.ylabel("Частота")
plt.grid(True)
plt.show()
