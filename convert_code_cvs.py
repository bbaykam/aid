import csv


a = []
with open("/home/basar/Downloads/icd10cm_codes_2020.txt") as f:
    for line in f :
        line = line.split(None, 1)
        line[1] = line[1][:-1]
        a.append(line)

with open("icd10cm_codes_2020.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(a)
