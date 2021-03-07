import csv
import random

csvFile = open("../../csv_fake_data.csv", 'w', newline='')
try:
    writer = csv.writer(csvFile)
    row = ['id', 'mental illness']
    for i in range(1, 10):
        string = "question"
        string += str(i)
        row.append(string)
    row.append('journal_indicator')
    writer.writerow(row)
    for i in range(100):
        level = random.randint(1, 4)
        row = [str(i), level]
        for j in range(10):
            row.append(level)
        writer.writerow(row)
finally:
    csvFile.close()
