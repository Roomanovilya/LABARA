import tkinter as tk
from tkinter import ttk
from itertools import product
import time
"""
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса.
Допускается использовать любую графическую библиотеку питона.
Пират хочет зарыть K кладов на  T островах. На каждом острове может быть зарыто не более M кладов.
Сформируйте разные варианты размещения кладов.
"""
"""
С помощью функций
"""
def generate_treasure_arrangements(K, T, M):
    a = list(product(range(T + 1), repeat=K))
    valid_arrangements = []  
    for arrangement in a:
        counts = [0] * (T + 1)
        for island in arrangement:
            if island != 0:
                counts[island] += 1
        if all(count <= M for count in counts[1:]):
            valid_arrangements.append(arrangement)
    return valid_arrangements

"""
Алгоритмический вариант
"""
def calculate_arrangements():
    K = int(entry_k.get())  
    T = int(entry_t.get())
    M = int(entry_m.get())
    start_time_algor = time.time()
    per = (T + 1) ** K  
    a = []
    for i in range(per):
        a1 = []
        i1 = i
        for _ in range(K):
            a1.append(i1 % (T + 1))
            i1 //= (T + 1)
        counts = [0] * (T + 1)
        for island in a1:
            if island != 0:
                counts[island] += 1
        if all(count <= M for count in counts[1:]):
            a.append(a1)
    end_time_algor = time.time()
    execution_time_algor = end_time_algor - start_time_algor

    start_time_function = time.time()
    valid_arrangements = generate_treasure_arrangements(K, T, M)
    end_time_function = time.time()
    execution_time_function = end_time_function - start_time_function
    
    if execution_time_algor < execution_time_function:
        comparison_result = f"Код (Алгоритмический вариант) быстрее на {execution_time_function - execution_time_algor:.6f} секунд."
    elif execution_time_algor > execution_time_function:
        comparison_result = f"Код с использованием функций быстрее на {execution_time_algor - execution_time_function:.6f} секунд."
    else:
        comparison_result = "Время выполнения кодов одинаково."

    result_label_algor.config(text=f"Время выполнения кода (Алгоритмический вариант): {execution_time_algor:.6f} секунд")
    result_label_func.config(text=f"Время выполнения кода с использованием функций: {execution_time_function:.6f} секунд")
    comparison_label.config(text=comparison_result)
    
    # Таблица
    for row in table.get_children():
        table.delete(row)
    
    header = ["Вариант"] + [f"Остров {i}" for i in range(1, T + 1)]
    table["columns"] = header
    table.heading("#0", text="", anchor="w")
    for col in header:
        table.heading(col, text=col, anchor="w")
        table.column(col, anchor="w", width=80)
    
    for idx, arrangement in enumerate(valid_arrangements):
        row = [f"Вариант {idx + 1}"]
        island_clads = [[] for _ in range(T)]
        for j, island in enumerate(arrangement):
            if island != 0:
                island_clads[island - 1].append(j + 1)
        
        for island in island_clads:
            if island:
                row.append(",".join(map(str, island)))
            else:
                row.append("0")
        
        table.insert("", "end", values=row)

#  основное окно
root = tk.Tk()
root.title("Пиратский клад")
root.configure(bg="#CD8162")

frame = tk.Frame(root, bg="#CD8162")
frame.pack(padx=10, pady=10)

# Создание меток и полей ввода для параметров распределения кладов
tk.Label(frame, text="Количество кладов (K):", bg="#CD8162").grid(row=0, column=0, padx=5, pady=5)
entry_k = tk.Entry(frame)
entry_k.grid(row=0, column=1, padx=5, pady=5)
entry_k.configure(bg="#EEDFCC")

tk.Label(frame, text="Количество островов (T):", bg="#CD8162").grid(row=1, column=0, padx=5, pady=5)
entry_t = tk.Entry(frame)
entry_t.grid(row=1, column=1, padx=5, pady=5)
entry_t.configure(bg="#EEDFCC")

tk.Label(frame, text="Максимальное количество кладов на одном острове (M):", bg="#CD8162").grid(row=2, column=0, padx=5, pady=5)
entry_m = tk.Entry(frame)
entry_m.grid(row=2, column=1, padx=5, pady=5)
entry_m.configure(bg="#EEDFCC")

#Кнопка для запуска расчетов
calculate_button = tk.Button(frame, text="Рассчитать", command=calculate_arrangements, bg="#EEDFCC")
calculate_button.grid(row=3, columnspan=2, padx=5, pady=5)

#Метки для вывода результатов выполнения и сравнения

result_label_algor = tk.Label(frame, text="", bg="#CD8162")
result_label_algor.grid(row=4, columnspan=2, padx=5, pady=5)

result_label_func = tk.Label(frame, text="", bg="#CD8162")
result_label_func.grid(row=5, columnspan=2, padx=5, pady=5)

comparison_label = tk.Label(frame, text="", bg="#CD8162")
comparison_label.grid(row=6, columnspan=2, padx=5, pady=5)

#Создание фрейма для таблицы с вариантами распределения кладов

table_frame = tk.Frame(root)
table_frame.pack(padx=10, pady=10, fill="both", expand=True)

#Настройка стилей для виджетов Treeview (таблицы с вариантами)

style = ttk.Style()
style.configure("Treeview", 
                background="#EEDFCC", 
                foreground="black",
                rowheight=25,
                fieldbackground="#EEDFCC")
style.map('Treeview', background=[('selected', '#CDB79E')], foreground=[('selected', 'white')])

#Создание и размещение Treeview для отображения вариантов распределения кладов

table = ttk.Treeview(table_frame, show="headings")
table.pack(side="left", fill="both", expand=True)

#Создание и размещение вертикального скроллбара для таблицы

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
scrollbar.pack(side="right", fill="y")
table.configure(yscrollcommand=scrollbar.set)


root.mainloop()
