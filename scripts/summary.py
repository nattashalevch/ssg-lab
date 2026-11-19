import csv
from collections import defaultdict

# Читаем исходные данные
with open("data/measurements.csv", encoding="utf-8") as file:
    data = list(csv.DictReader(file))

groups = defaultdict(list)

for row in data:
    groups[row["group"]].append(row)

# Подготавливаем таблицу
lines = [
    "# Сводные результаты эксперимента",
    "",
    "Средние значения показателей за 8 учебных недель.",
    "",
    "| Группа | Вовлечённость | Выполнение заданий, % | Взаимодействия |",
    "|---|---:|---:|---:|",
]

names = {
    "control": "Контрольная",
    "gamified": "Геймифицированная",
}

for group_name, rows in groups.items():
    count = len(rows)
    engagement = sum(float(r["engagement_score"]) for r in rows) / count
    completion = sum(float(r["task_completion"]) for r in rows) / count
    interactions = sum(float(r["interactions"]) for r in rows) / count

    lines.append(
        f"| {names[group_name]} | {engagement:.2f} | "
        f"{completion:.2f} | {interactions:.2f} |"
    )

lines += [
    "",
    "> Данные синтетические и предназначены для демонстрации работы конвейера.",
    "",
]

# Сохраняем таблицу в файл сайта
with open("docs/results.md", "w", encoding="utf-8") as file:
    file.write("\n".join(lines))

print("Таблица создана: docs/results.md")
