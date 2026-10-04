import csv
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt

csv_path = Path(__file__).with_name("HR Dataset.csv")

with csv_path.open(newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    status_counts = Counter(
        row["Employment Status"].strip()
        for row in reader
        if row["Employment Status"].strip()
    )

statuses = list(status_counts.keys())
counts = list(status_counts.values())

plt.pie(
    counts,
    labels=statuses,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Employee Employment Status Breakdown")
plt.axis("equal")
plt.show()