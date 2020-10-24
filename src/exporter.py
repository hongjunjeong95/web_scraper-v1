import csv


def save_to_file(jobs, word):
    file_name = f"{word}.csv"
    file = open(file_name, mode="w", encoding="utf-8")
    fieldnames = ["title", "company", "location", "link"]
    writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for job in jobs:
        writer.writerow(job)
