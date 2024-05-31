import csv
import math
from create_Vtable import create_Vtable as create_Vtable
import os

password = input("What is your password? ")
cyphertext = input("What is the cypthertext? ")

password = password.upper()

vtable = create_Vtable(password)

reps = math.ceil(len(cyphertext) / len(password))
key = ''
for i in range(reps):

    key = key + password

key = key[:len(cyphertext)]
decrpytedmessage = ''

for i in range(len(cyphertext)):

    # get letter from key
    y = key[i]
    #print("y: "+y)

    # get that letters index in y-column
    n = vtable[0].index(y)
    #print("n: "+str(n))
    # get that row
    row = vtable[n]
    #print("row: ")
    stringrow = ''
    for l in row:
        stringrow = stringrow + l
    #print(stringrow)

    # slice off the first letter before searching the row for cypherletter
    m = row[1:].index(cyphertext[i]) + 1
    #print("m: "+str(m))
    decryptedletter = vtable[0][m]
    #print("decrypted letter: "+decryptedletter)
    decrpytedmessage = decrpytedmessage + decryptedletter

print(decrpytedmessage)

# delete old Vtable
file_path = '/Users/ericscalibur/Documents/encryption-py/Vtable.csv'
if os.path.exists(file_path):
    os.remove(file_path)
    print("Vtable deleted")
