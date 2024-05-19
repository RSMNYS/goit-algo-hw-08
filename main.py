import heapq

def min_cost_to_connect_cables(data):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(data)
    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(data) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(data)
        second = heapq.heappop(data)
        # Витрати на з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost
        # Вставляємо новий кабель назад у купу
        heapq.heappush(data, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
minimum_cost = min_cost_to_connect_cables(cables)
print("Minimum cost to connect cables:", minimum_cost)
