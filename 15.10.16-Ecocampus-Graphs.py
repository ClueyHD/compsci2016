# Ecocampus Plotting Code
# 2016 Kyle Choi

import csv


names = []
count = 0

name = []
counts = []

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
    if c in name:
        #count.append(name.index(c))
        print(name.index(c))
        counts.insert(name.index(c), counts[name.index(c)]+1)
    else:
        name.append(c)
        counts.append(1)
print(name)
print(counts)
