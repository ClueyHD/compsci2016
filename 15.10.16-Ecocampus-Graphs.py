# Ecocampus Plotting Code
# 2016 Kyle Choi

import csv

names = []
count = 0

file_open = "data.csv"

data = open(file_open)
data = csv.reader(data)
data = list(data)

for i in data:
    if count == 0:
        count += 1
        headers = i
    else:
        names.append(i[11])

for c in names:
    print(c)