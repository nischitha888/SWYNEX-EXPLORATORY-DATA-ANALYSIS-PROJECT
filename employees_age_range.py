import csv
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

csv_path = Path(__file__).with_name("HR Dataset.csv")

counts = Counter()

with csv_path.open(newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        age_range = row["Age range"].strip()
        gender = row["Gender"].strip().lower()

        if age_range and gender in ("male", "female"):
            counts[(age_range, gender)] += 1

# Keep age ranges in the order they appear in the CSV
age_ranges = list(dict.fromkeys(age for age, _ in counts))
male_counts = [counts[(age, "male")] for age in age_ranges]
female_counts = [counts[(age, "female")] for age in age_ranges]

x = np.arange(len(age_ranges))
bar_width = 0.35

plt.bar(x - bar_width / 2, male_counts, bar_width, label="Male")
plt.bar(x + bar_width / 2, female_counts, bar_width, label="Female")

plt.title("Employees by Age Range and Gender")
plt.xlabel("Age Range")
plt.ylabel("Number of Employees")
plt.xticks(x, age_ranges)
plt.legend()
plt.tight_layout()
plt.show()