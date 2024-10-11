import os

try:
    with open('testdata.txt','r') as file:
        content = file.readlines()
        print(content)
except FileNotFoundError as fnfe:
    print(fnfe)

finally: #try and except is present inside finally block
    try:
        file.close()
    except NameError as ne:
        print("NE")