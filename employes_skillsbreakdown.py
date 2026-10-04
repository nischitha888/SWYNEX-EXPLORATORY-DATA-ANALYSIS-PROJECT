import csv
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt

csv_path = Path(__file__).with_name("HR Dataset.csv")

with csv_path.open(newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    skills_count = Counter(
        row["Skills"].strip()
        for row in reader
        if row["Skills"].strip()
    )

skills = list(skills_count.keys())
counts = list(skills_count.values())

plt.bar(skills, counts)
plt.title("Employee Skills Breakdown")
plt.xlabel("Skill")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()