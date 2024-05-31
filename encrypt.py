import string
import math
from create_Vtable import create_Vtable as create_Vtable
from print_Vtable import print_Vtable as print_Vtable
import os

password = input("What is your password? ")

# password cannot contain repeating letters
while len(set(password)) != len(password):
    print("Password cannot contain repeat letters.")
    password = input("What is your password? ")

plaintext = input("What message do you want to encrypt? ")
plaintext = plaintext.replace(' ', '')
# replace spaces with 0
# space = ' '
# for space in plaintext:
#
#     plaintext.replace(space, '0')


# convert strings to all uppercase characters
password = password.upper()
plaintext = plaintext.upper()
#print(plaintext)
vtable = create_Vtable(password)

# print_Vtable(vtable)

def encrypt_text(pt, pw, vt):

    key = ''
    # how many times to repeat the password (pw)
    # to match the length of the plaintext (pt)
    reps = math.ceil(len(pt) / len(pw))

    for i in range(reps):

        key = key + pw

    key = key[:len(pt)]
    # print(key)

    # 'coordinates' in vtable
    x = ''
    y = ''
    cyphertext = ''

    # get x-coord
    for i in range(len(pt)):
        # print(pt[i])
        # print(vtable[0])

        # print("x: "+str(x))
        y = vtable[0].index(key[i])

        # print("Plaintext Letter: "+str(pt[i]))
        # print("x: "+str(x))
        # print("Key Letter: "+str(key[i]))
        # print("y: "+str(y))

        if pt[i] == ' ':
            x = 0
        else:
            x = vtable[0].index(pt[i])

        cypherletter = vtable[y][x]
        # print("cypherletter: "+cypherletter)
        cyphertext = cyphertext + cypherletter

    return cyphertext

encryptedText = encrypt_text(plaintext, password, vtable)
print("Here is your encrypted text: "+encryptedText)

# delete old Vtable
# file_path = '/Users/ericscalibur/Documents/encryption-py/Vtable.csv'
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print("Vtable deleted")
