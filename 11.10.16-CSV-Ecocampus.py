# EarthWatch Correction Code
# 2016 Kyle Choi

import csv

count = 0
names = []
names_storage = []
names_corrected = []

#file_open = input("Please the filename of the document to be read by the program (e.g. magpie.csv)")
file_open = "C:\\Users\Kyle\PycharmProjects\compsci2016\sample_data\magpie.csv"

data = open(file_open)
data = csv.reader(data)
data = list(data)

for i in data:
    if count == 0:
        count += 1
        headers = i
    else:
        names.append(i[2])
        #print(i[2])

def name_adjust(original,correct):
    confirm = input("Would you like the script to remember '"+correct+"'? (y/n) ")
    if confirm == "y":
        names_storage.append(original)
        names_corrected.append(correct)
    return


"""
ideas - auto capitalise, correct names
"""
b = " "
for c in names:
    if c in names_storage:
        c=names_corrected[names_storage.index(c)]
        print(c)
    else:
        #c=string.capwords(c)
        print(c)
        a=c.split(" ")
        print(len(a))
        if len(a) == 3 or 4: # duplicate name error checking
            print("possible name error")


            if a[0] in a[1:]: # checks if first name is duplicated
                var = True
                while var:
                    name_inp = input("A first name is repeated in: '"+b.join(a)+"' Would you like to remove the duplicate? (y/n) ")
                    if name_inp == "y":
                        var1 = True
                        while var1:
                            print(len(a[0]))
                            name_conf = input("the new name is '"+c[(len(a[0])+1):]+"' is this correct? ")
                            if name_conf == "y":
                                print(c[(len(a[0])+1):])
                                name_adjust(c,c[(len(a[0])+1):])
                                var = False
                                var1 = False
                            elif name_conf == "n":
                                name_change = input("Please enter the name manually")
                                name_conf1 = input("the new name is '" + name_change + "' is this correct? (y/n) ")
                                if name_conf1 == "y":
                                    print(name_change)
                                    name_adjust(c,name_change)
                                    var = False
                                    var1 = False
                            elif name_adjust == "s":
                                print("test")
                            else:
                                print("I'm sorry that's not a valid entry, please enter one of the following without quotation marks, yes 'y', no 'n' or skip 's' ")
                    elif name_inp == "n":
                        var = False
                        name_conf = input("Would you like the script to remember '"+c+"' ")
                        if name_conf == "y":
                            print(c)
                            names_storage.append(c)
                            names_corrected.append(c)
                    else:
                        print("I'm sorry that's not a valid entry, please enter one of the following without quotation marks, yes 'y' or no 'n' ")


            elif a[-1] in a [:-2]: # checks if last name is duplicated
                name_inp = input("A last name is repeated in: '"+b.join(a)+"' Would you like to remove the duplicate? (y/n) ")
                if name_inp == "y":
                    print(len(a[-1]))
                    name_conf = input("the new name is '" + c[:(len(a[-1])-1)] + "' is this correct? ")
                    if name_conf == "y":
                        print(c[:(len(a[-1])-1)])
                        name_adjust(c,c[:(len(a[-1])-1)])



        elif len(a) >= 5:
            var = True
            while var:
                name_inp = input("It seems '"+c+"' is an unusually large string, would you like to modify it? (y/n) ")
                if name_inp == "y":
                    name_change=input("Please input a new name for this entry: ")
                elif name_inp == "n":
                    var = False
                else:
                    print("I'm sorry that's not a valid entry, please enter one of the following without quotation marks, yes 'y' or no 'n' ")


        else:
            print("Pass")

#print(headers)
