import csv


def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="utf-8")
    fieldnames = ["title", "company", "location", "link"]
    writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()

    for job in jobs:
        writer.writerow(job)
