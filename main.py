import json


data = []

# Чтение из исходного файла и создание списка словарей
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, price, action = line.strip().split()
        price = int(price)
        name = str(name)
        action = bool(action)
        data.append({'Название товара': name, 'Цена': price, 'Акция': action})

# Сортировка списка по названию товара в алфавитном порядке
data.sort(key=lambda x: x['Название товара'])

# Запись списка словарей в новый текстовый файл output1.txt
with open('output1.txt', 'w', encoding='utf-8') as file:
    for item in data:
        file.write(f"{item['Название товара']}{item['Цена']}{item['Акция']} \n")

# Запись списка словарей в json файл
with open('output2.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)

# Чтение из json и запись списка словарей
with open('output2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Сортировка по возрастанию цены товара
data.sort(key=lambda x: x['Цена'])

# Запись списка словарей в новый текстовый файл  output3.txt
with open('output3.txt', 'w', encoding='utf-8') as file:
    for item in data:
        file.write(f"{item['Название товара']}{item['Цена']}{item['Акция']} \n")
