import csv

CSV_PATH = "rocstories.csv"
TXT_PATH = "rocstories.txt"

sentences = ""
with open(CSV_PATH, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        for i in range(1, 6):
            sentences += row[i] + "\n"

with open(TXT_PATH, mode="w", encoding="utf-8") as f:
    f.write(sentences)
