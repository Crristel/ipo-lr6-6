import random #подключаем модуль random
spisok=[(random.randint(-10,10),random.randint(-10,10),random.randint(-10,10),random.randint(-10,10)) for i in range(1,20+1)] #с помощью генератора списка создаём список с числами в диапазоне от -10 до 10
print (spisok)
unique_pairs=set()

for i in range(len(spisok)):
    for j in range(i + 1, len(spisok)):
        # Создаем кортеж из двух элементов и добавляем в множество для уникальности
        unique_pairs.add((spisok[i], spisok[j]))



# Выводим список кортежей
print("Список уникальных пар:")
for pair in unique_pairs:
    print(pair)

# Пользователь вводит целое число
user_input = int(input("Введите целое число: "))

# Вычисляем количество пар, чья сумма меньше заданного значения
count = 0
for pair in unique_pairs:
    sum_pair = sum(pair[0]) + sum(pair[1])
    if sum_pair < user_input:
        count += 1

# Выводим результат
print(f"Количество пар, чья сумма меньше {user_input}: {count}")


