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
#

# Set variables
names = []
count = 0
head = 1

name = []
counts = []
headers = " "

file_open = "data.csv"
#

data = open(file_open)
data = csv.reader(data)
data = list(data)

print(colour.RED+"*DISCLAIMER* This software has not been tested by anyone but the writer themselves, therefore it should be considered BETA software and may contain bugs. "+colour.END)
print(colour.RED+"This software is covered under the GPL, therefore the author takes no responsibility for any problems arising from the use of this software. "+colour.END)
print(colour.RED+"I am not responsible for the destruction of your computer"+colour.END)
print(colour.GREEN+"Welcome to the Monash Ecocampus Data Analysis Program!"+colour.END)
print(colour.UNDERLINE+"Your CSV contains the following columns: "+colour.END)
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
            print(colour.RED+"Sorry, that is not a valid number, please pick an integer between 1 and " + str(head - 1) + ": "+colour.END)
    except ValueError:
        print(colour.RED+"Sorry, that is not a valid character, please pick an integer between 1 and "+str(head-1)+": "+colour.END)

# Take out headers & append data values to 'name'
for i in data:
    if count == 0:
        count += 1
        headers = i
    else:
        names.append(i[int(option1)-1])
#

# Core sorting code
for c in names:
    c = c.replace('  ', ' ')
    if c in name:
        # count.append(name.index(c))
        # print(name.index(c))
        counts[name.index(c)] = int(counts[name.index(c)]+1)
        # counts.insert(name.index(c), int(counts[name.index(c)]+1))
    else:
        name.append(c)
        counts.append(1)
name = [element or "Not Defined" for element in name]
#

print(colour.GREEN + "What would you like to do with this data?" + colour.END)
print("a: Plot a graph")
print("b: Export individual column to CSV")
var = True
while var:
    option = input("Please pick on option (a/b): ")
    if option == "a":
        # Bar graph plotting
        print("Plotting graph... please wait")
        plotly.offline.plot({
            "data": [Bar(x=name, y=counts)],
            "layout": Layout(title="'" + headers[14] + "' bar graph")
        })
        var = False
        #

    elif option == 'b':
        # Export to CSV
        print("hello")


# print(name)
# print(counts)

print("Done!")
