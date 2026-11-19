import csv
from collections import defaultdict

# Читаем исходные данные
with open("data/measurements.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Собираем показатели по группам
groups = defaultdict(list)

for row in data:
    groups[row["group"]].append(row)

# Вычисляем средние значения
print("Результаты эксперимента")
print("-" * 40)

for group_name, rows in groups.items():
    avg_engagement = sum(
        float(row["engagement_score"]) for row in rows
    ) / len(rows)

    avg_completion = sum(
        float(row["task_completion"]) for row in rows
    ) / len(rows)

    avg_interactions = sum(
        float(row["interactions"]) for row in rows
    ) / len(rows)

    print(f"\nГруппа: {group_name}")
    print(f"Средняя вовлечённость: {avg_engagement:.2f}")
    print(f"Среднее выполнение заданий: {avg_completion:.2f}%")
    print(f"Среднее число взаимодействий: {avg_interactions:.2f}")
