# Ecocampus Plotting Code
# 2016 Kyle Choi

import csv
import plotly
from plotly.graph_objs import Bar, Layout

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
        names.append(i[14])

for c in names:
    if c in name:
        #count.append(name.index(c))
        c = c.replace('  ', ' ')
        #print(name.index(c))
        counts[name.index(c)] = int(counts[name.index(c)]+1)
        #counts.insert(name.index(c), int(counts[name.index(c)]+1))
    else:
        name.append(c)
        counts.append(1)
#print(name)
#print(counts)

plotly.offline.plot({
    "data": [Bar(x=name, y=counts)],
    "layout": Layout(title="hello world")
})