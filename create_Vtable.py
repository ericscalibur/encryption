import math
import string
import csv

capitals = string.ascii_uppercase
firstrow = '0' + capitals + ' '

def create_Vtable(p):
    vtable = [firstrow]
    vrow = []

    for letter in p:
        vrow.append(letter)

    for letter in capitals:

        if letter not in p:

            vrow.append(letter)

    for i in range(len(capitals)):
        newvrow = list(capitals[i]) + vrow[-i:] + vrow[:-i]
        vtable.append(newvrow)

    for row in vtable:
        string = ""
        for letter in row:
            string = string + letter

    with open('Vtable.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(vtable)

    return vtable
