import csv
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt

# Find the CSV file in the same folder as this Python script
csv_path = Path(__file__).with_name("HR Dataset.csv")

# Count employees in each region
region_counts = Counter()

with csv_path.open(newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        region = row["Region"].strip()
        if region:
            region_counts[region] += 1

regions = list(region_counts.keys())
employee_counts = list(region_counts.values())

# Draw the bar graph
plt.bar(regions, employee_counts, color="steelblue")
plt.title("Employees by Region")
plt.xlabel("Region")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()