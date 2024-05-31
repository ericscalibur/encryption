import csv

def print_Vtable(vtable):

    for row in vtable:
        string = ""
        for letter in row:

            string = string + letter

        print(string+"\n")
