import os

try:
    file = open('testdata.txt','r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("no such file present, fix the path or create the file")

finally: #try and except is present inside finally block
    try:
        file.close()
    except NameError as ne:
        print(ne)
