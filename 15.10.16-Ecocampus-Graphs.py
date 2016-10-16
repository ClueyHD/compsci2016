# Ecocampus Plotting Code
# 2016 Kyle Choi

print("Loading... please wait")
import csv
import plotly
from plotly.graph_objs import Bar, Layout

# yay colours
class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Set variables
names = []
count = 0
head = 1

name = []
counts = []
headers = " "

print(colour.RED+"*DISCLAIMER* This software has not been tested by anyone but the writer themselves, therefore it should be considered BETA software and may contain bugs. "+colour.END)
print(colour.RED+"This software is covered under the GPL, therefore the author takes no responsibility for any problems arising from the use of this software. "+colour.END)
print(colour.RED+"I am not responsible for the destruction of your computer. "+colour.END)
print(colour.GREEN+"Welcome to the Monash Ecocampus Data Analysis Program!"+colour.END)

var = True
while var:
    try:
        file_input = input(colour.BLUE+"Please enter the name of the csv file "+colour.YELLOW+"(excluding the .csv extension): "+colour.END)
        file_open = file_input + ".csv"
        data = open(file_open)
        data = csv.reader(data)
        data = list(data)
        var = False
    except FileNotFoundError:
        print(colour.RED+"ERROR: that file does not exist, please check the filename and try again. "+colour.END)

print(colour.UNDERLINE+"Your CSV contains the following columns:"+colour.END+" ")
for i in data[0]:
    print(str(head)+" '"+i+"'")
    head += 1
var = True
while var:
    option1 = input(colour.BLUE+"Please select a column to use in the program (1-"+str(head-1)+"): "+colour.END)
    try:
        if (1 <= int(option1) <= head-1):
            var = False
        else:
            print(colour.RED+"ERROR: that is not a valid number, please pick an integer between 1 and " + str(head - 1) + ": "+colour.END)
    except ValueError:
        print(colour.RED+"ERROR: that is not a valid character, please pick an integer between 1 and "+str(head-1)+": "+colour.END)

# Take out headers & append data values to 'name'
for i in data:
    if count == 0:
        count += 1
        headers = i
    else:
        names.append(i[int(option1)-1])

# Core sorting code
for c in names:
    c = c.replace('  ', ' ')
    if c in name:
        counts[name.index(c)] = int(counts[name.index(c)]+1)
    else:
        name.append(c)
        counts.append(1)
name = [element or "Not Defined" for element in name]


var = True
while var:
    print(colour.GREEN + "What would you like to do with this data?" + colour.END)
    print("a: Plot a graph")
    print("b: Export individual column to CSV")
    option = input("Please pick on option (a/b): ")
    if option == "a":
        # Bar graph plotting
        print("Plotting graph... please wait")
        plotly.offline.plot({
            "data": [Bar(x=name, y=counts)],
            "layout": Layout(title="'" + headers[14] + "' bar graph")
        })
        var = False

    elif option == 'b':
        # Export to CSV
        # Assuming res is a flat list
        var1 = True
        while var1:
            try:
                newcsv_name = input("Please enter a name for the new csv file "+colour.YELLOW+"(excluding the .csv extension): "+colour.END)
                newcsv = newcsv_name+".csv"
                try:
                    with open(newcsv, "w", newline='') as csvout:
                        writer = csv.writer(csvout, lineterminator='\n')
                        writer.writerow([str(headers[int(option1)-1]),"count"])
                        rows = zip(name,counts)
                        for z in rows:
                            writer.writerow(z)
                    var = False
                    var1 = False
                except PermissionError:
                    print(colour.RED+'ERROR: It seems the CSV file you are trying to write to is already open in another program, please close it amd try again. ')
            except OSError:
                print(colour.RED+"ERROR: That is not a valid file name, please make sure you are using valid characters in the filename and try again "+colour.YELLOW+'(\/:*?"<>| are not valid characters in Windows). '+colour.END)
    else:
        print(colour.RED+'ERROR: That is not a valid character, please enter "a" or "b" (no quotations)'+colour.END)

print("Done!")
