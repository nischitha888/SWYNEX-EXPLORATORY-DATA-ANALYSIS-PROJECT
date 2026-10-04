import csv
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt

csv_path = Path(__file__).with_name("HR Dataset.csv")
leave_by_job = Counter()

with csv_path.open(newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        job_title = row["Job Title"].strip()
        leave_text = row["Leave Taken"].strip()

        if job_title and leave_text:
            leave_by_job[job_title] += int(leave_text)

job_titles = list(leave_by_job.keys())
total_leave = list(leave_by_job.values())

plt.figure(figsize=(10, 6))
plt.bar(job_titles, total_leave, color="steelblue")
plt.title("Total Leave Taken by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Total Leave Taken")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()