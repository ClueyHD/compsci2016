# Filter Categories
# 2016 Kyle Choi

import csv
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_open = filedialog.askopenfilename()
data = open(file_open)
data = csv.reader(data)
data = list(data)
count = 0
species = []
time = []
lat = []
long = []

for a in data:
    if count == 0:
        headers = a
        count += 1
    else:
        species.append(a[14])
        time.append(a[37])
        lat.append(a[22])
        long.append(a[23])

listing = zip(species, time, lat, long)

newcsv = "data.trim.csv"
with open(newcsv, "w", newline='') as csvout:
    writer = csv.writer(csvout, lineterminator='\n')
    writer.writerow([headers[14], headers[37], headers[22], headers[23]])
    for k in listing:
        writer.writerow(k)
