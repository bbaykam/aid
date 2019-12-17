import csv


output = set()
with open("/home/basar/Downloads/icd10cm_codes_2020.txt") as f:
    for line in f :
        line = line.split(None, 1)
        if line[0].startswith('S') :
            line[0] = line[0][:3]
            output.add(line[0])

print(list(output))
print(len(output))
