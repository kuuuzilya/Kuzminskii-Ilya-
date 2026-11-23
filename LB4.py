def solve_backpack(start_points, rows, cols, items, mandatory_item):    #исходные данные
    capacity = rows * cols  #начальная вместимость

    total_all_items = sum(val for size, val in items.values())  #суммарная ценность всех предметов

    mand_size, mand_val = items[mandatory_item]   #выбираем обязательный предмет
    rem_capacity = capacity - mand_size           #оставшиеся свободные ячейки

    other_items = [(code, size, val) for code, (size, val) in items.items() if code != mandatory_item]  #оставшиеся предметы
    n = len(other_items)

    dp = [[0] * (rem_capacity + 1) for k in range(n + 1)]  #таблица динамического программирования

    for i in range(1, n + 1):   #перебор оставшихся предметов (строк таблицы)
        code, size, val = other_items[i - 1]
        for w in range(rem_capacity + 1): #перебор вместимостей (столбцов таблицы)
            if size <= w:  #если размер предмета помещается в текущую вместимость
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - size] + val)
            else:
                dp[i][w] = dp[i - 1][w]

    chosen = [(mandatory_item, mand_size)]  #восстанавливаем список взятых предметов
    w = rem_capacity
    for i in range(n, 0, -1):   #перебираем таблицу с конца
        if dp[i][w] != dp[i - 1][w]:     #если ценность текущей строки изменилась относительно предыдущей
            code, size, val = other_items[i - 1]
            chosen.append((code, size))
            w -= size

    taken_points = mand_val + dp[n][rem_capacity]
    untaken_points = total_all_items - taken_points
    final_score = start_points + taken_points - untaken_points  #подсчет итоговых очков

    if final_score <= 0:
        print(f"Положительный счет невозможен. Максимум: {final_score}")
        return

    flat_inventory = []   #формируем двумерный массив (инвентарь)
    for code, size in chosen:
        flat_inventory.extend([code] * size)

    for r in range(rows):   #вывод результата
        row_cells = [f"[{flat_inventory[r * cols + c]}]" for c in range(cols)]
        print(",".join(row_cells))

    print(f"\nИтоговые очки выживания: {final_score}")


#исходные данные
rows, cols = 3, 3
start_points = 15
mandatory_item = 'd'  # антидот от паранойи
items = {
    'r': (3, 25),  # Винтовка
    'p': (2, 15),  # Пистолет
    'a': (2, 15),  # Боекомплект
    'm': (2, 20),  # Аптечка
    'i': (1, 5),  # Ингалятор
    'k': (1, 15),  # Нож
    'x': (3, 20),  # Топор
    't': (1, 25),  # Оберег
    'f': (1, 15),  # Фляжка
    'd': (1, 10),  # Антидот
    's': (2, 20),  # Еда
    'c': (2, 20)}  # Арбалет

solve_backpack(start_points, rows, cols, items, mandatory_item)