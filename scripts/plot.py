import csv
import matplotlib.pyplot as plt

# Загружаем данные из CSV
with open("data/measurements.csv", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

# Разделяем данные по группам
control = [row for row in rows if row["group"] == "control"]
gamified = [row for row in rows if row["group"] == "gamified"]

weeks_control = [int(row["week"]) for row in control]
scores_control = [int(row["engagement_score"]) for row in control]

weeks_gamified = [int(row["week"]) for row in gamified]
scores_gamified = [int(row["engagement_score"]) for row in gamified]

# Строим график
plt.figure(figsize=(10, 6))

plt.plot(weeks_control, scores_control, marker="o", label="Контрольная группа")
plt.plot(weeks_gamified, scores_gamified, marker="o", label="Геймификация")

plt.title("Динамика вовлечённости студентов")
plt.xlabel("Учебная неделя")
plt.ylabel("Индекс вовлечённости (0–100)")
plt.xticks(range(1, 9))
plt.ylim(0, 100)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

# Создаём папку и сохраняем график для сайта
import os
os.makedirs("docs/images", exist_ok=True)
plt.savefig("docs/images/engagement.png", dpi=150)

print("График успешно создан: docs/images/engagement.png")
