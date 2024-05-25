'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 19. Пират хочет зарыть К кладов на Т островах. Сформируйте разные варианты размещения кладов.
'''
import time
from itertools import product

# Ввод значений K и T
K = int(input("Введите количество кладов (K): "))
T = int(input("Введите количество островов (T): "))

"""
-----ЧАСТЬ 1-----
"""
print('-----ЧАСТЬ 1-----')
"""
Алгоритмический вариант
"""
start_time_algor = time.time()

# Подсчет количества переборов
per = (T + 1) ** K

# Создание всех возможных вариантов размещения кладов
a = []
for i in range(per):
    a1 = []
    i1 = i
    for _ in range(K):
        a1.append(i1 % (T + 1))
        i1 //= (T + 1)
    a.append(a1)

end_time_algor = time.time()
execution_time_algor = end_time_algor - start_time_algor
print(f"Время выполнения кода (Алгоритмический вариант): {execution_time_algor:.6f} секунд")

"""
С помощью функций
"""
start_time_function = time.time()

def generate_treasure_arrangements(K, T):

    # Создание всех возможных вариантов размещения кладов
    a = list(product(range(T + 1), repeat=K))
    return a

a = generate_treasure_arrangements(K, T)

end_time_function = time.time()
execution_time_function = end_time_function - start_time_function
print(f"Время выполнения кода с использованием функций: {execution_time_function:.6f} секунд")

if execution_time_algor < execution_time_function:
    print(f"Код (Алгоритмический вариант) быстрее на {execution_time_function - execution_time_algor:.6f} секунд.")
elif execution_time_algor > execution_time_function:
    print(f"Код с использованием функций быстрее на {execution_time_algor - execution_time_function:.6f} секунд.")
else:
    print("Время выполнения кодов одинаково.")
    
want_table = input("Хотите вывести таблицу? (1 - ДА, 0 - НЕТ): ")
if want_table == "1":
    # Заголовок таблицы
    header = ["№ острова"] + [str(i) for i in range(1, T + 1)]

    # Определяем максимальную длину строки для разделения
    max_length = max(len(word) for word in header)
    separator = "+" + "+".join(["-" * max_length for _ in header]) + "+"

    # Печатаем заголовок таблицы
    print(separator)
    print("|" + "|".join(f"{word:^{max_length}}" for word in header) + "|")
    print(separator.replace("-", "="))

    # Печатаем все варианты размещения кладов
    for idx, a1 in enumerate(a):
        row = [f"Вариант {idx + 1}"]
        island_clads = [[] for _ in range(T)]
        for j, island in enumerate(a1):
            if island != 0:
                island_clads[island - 1].append(j + 1)

        for island in island_clads:
            if island:
                row.append("".join(map(str, island)))
            else:
                row.append("0")

        print("|" + "|".join(f"{word:^{max_length}}" for word in row) + "|")
        print()
else:
    print("Таблица не будет выведена.")

"""
-----ЧАСТЬ 2-----
"""
print('-----ЧАСТЬ 2-----')

'''
Ограничение:
Пират хочет зарыть K кладов на  T островах. На каждом острове может быть зарыто не более M кладов. Сформируйте разные варианты размещения кладов.
'''

M = int(input("Введите максимальное количество кладов на одном острове (M): "))

"""
Алгоритмический вариант
"""
start_time_algor = time.time()

# Подсчет количества переборов
per = (T + 1) ** K

# Создание всех возможных вариантов размещения кладов с ограничением на M кладов
a = []
for i in range(per):
    a1 = []
    i1 = i
    for _ in range(K):
        a1.append(i1 % (T + 1))
        i1 //= (T + 1)
    # Проверка ограничения на M кладов
    counts = [0] * (T + 1)
    for island in a1:
        if island != 0:
            counts[island] += 1
    if all(count <= M for count in counts[1:]):
        a.append(a1)

end_time_algor = time.time()
execution_time_algor = end_time_algor - start_time_algor
print(f"Время выполнения кода (Алгоритмический вариант): {execution_time_algor:.6f} секунд")

"""
С помощью функций
"""
start_time_function = time.time()

def generate_treasure_arrangements(K, T, M):
    # Создание всех возможных вариантов размещения кладов
    a = list(product(range(T + 1), repeat=K))
    
    # Фильтрация вариантов, удовлетворяющих ограничению на M кладов
    valid_arrangements = []
    for arrangement in a:
        counts = [0] * (T + 1)
        for island in arrangement:
            if island != 0:
                counts[island] += 1
        if all(count <= M for count in counts[1:]):
            valid_arrangements.append(arrangement)
    
    return valid_arrangements

valid_arrangements = generate_treasure_arrangements(K, T, M)

end_time_function = time.time()
execution_time_function = end_time_function - start_time_function
print(f"Время выполнения кода с использованием функций: {execution_time_function:.6f} секунд")

if execution_time_algor < execution_time_function:
    print(f"Код (Алгоритмический вариант) быстрее на {execution_time_function - execution_time_algor:.6f} секунд.")
elif execution_time_algor > execution_time_function:
    print(f"Код с использованием функций быстрее на {execution_time_algor - execution_time_function:.6f} секунд.")
else:
    print("Время выполнения кодов одинаково.")

want_table = input("Хотите вывести таблицу? (1 - ДА, 0 - НЕТ): ")
if want_table == "1":
    # Заголовок таблицы
    header = ["№ острова"] + [str(i) for i in range(1, T + 1)]

    # Определяем максимальную длину строки для  разделения
    max_length = max(len(word) for word in header)
    separator = "+" + "+".join(["-" * max_length for _ in header]) + "+"

    # Печатаем заголовок таблицы
    print(separator)
    print("|" + "|".join(f"{word:^{max_length}}" for word in header) + "|")
    print(separator.replace("-", "="))

    # Печатаем все варианты размещения кладов
    for idx, a1 in enumerate(valid_arrangements):
        row = [f"Вариант {idx + 1}"]
        island_clads = [[] for _ in range(T)]
        for j, island in enumerate(a1):
            if island != 0:
                island_clads[island - 1].append(j + 1)

        for island in island_clads:
            if island:
                row.append("".join(map(str, island)))
            else:
                row.append("0")

        print("|" + "|".join(f"{word:^{max_length}}" for word in row) + "|")
        print()
else:
    print("Таблица не будет выведена.")
