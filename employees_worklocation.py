import csv
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt

csv_path = Path(__file__).with_name("HR Dataset.csv")

with csv_path.open(newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    location_counts = Counter(
        row["Work Location"].strip()
        for row in reader
        if row["Work Location"].strip()
    )

locations = list(location_counts.keys())
counts = list(location_counts.values())

plt.bar(locations, counts)
plt.title("Employees by Work Location")
plt.xlabel("Work Location")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()