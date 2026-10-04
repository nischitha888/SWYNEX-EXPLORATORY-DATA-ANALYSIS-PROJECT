import csv
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt

# Find the CSV file in the same folder as this Python script
csv_path = Path(__file__).with_name("HR Dataset.csv")

# Count employees by gender
gender_counts = Counter()

with csv_path.open(newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        gender = row["Gender"].strip().title()
        if gender in ("Male", "Female"):
            gender_counts[gender] += 1

# Create two pie charts
fig, axes = plt.subplots(1, 2, figsize=(9, 4))

chart_details = [
    ("Male", "♂", "blue"),
    ("Female", "♀", "orange"),
]

for ax, (gender, symbol, color) in zip(axes, chart_details):
    count = gender_counts[gender]

    ax.pie([count], colors=[color], startangle=90)
    ax.text(
        0, 0,
        f"{symbol}\n{gender}\n{count} employees",
        ha="center",
        va="center",
        fontsize=15
    )
    ax.set_title(f"{gender} Employees")
    ax.axis("equal")

plt.suptitle("Employee Gender Counts")
plt.tight_layout()
plt.show()