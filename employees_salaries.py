import csv
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt

csv_path = Path(__file__).with_name("HR Dataset.csv")
salary_by_job = defaultdict(float)

with csv_path.open(newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        job_title = row["Job Title"].strip()
        salary_text = row["Salary"].strip().replace(",", "")

        if job_title and salary_text:
            salary_by_job[job_title] += float(salary_text)

job_titles = list(salary_by_job.keys())
salary_totals = list(salary_by_job.values())

# Format salary amounts using Indian digit grouping, e.g. ₹1,23,456
def inr(amount):
    whole = str(int(round(amount)))
    if len(whole) > 3:
        last_three = whole[-3:]
        remaining = whole[:-3]
        groups = []
        while remaining:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        whole = ",".join(groups) + "," + last_three
    return f"₹{whole}"

labels = [
    f"{job}\n{inr(total)}"
    for job, total in zip(job_titles, salary_totals)
]

plt.figure(figsize=(10, 8))
plt.pie(
    salary_totals,
    labels=labels,
    startangle=90
)
plt.title("Total Employee Salaries by Job Role (INR)")
plt.axis("equal")
plt.tight_layout()
plt.show()