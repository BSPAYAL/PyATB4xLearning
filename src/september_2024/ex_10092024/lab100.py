#if file is not present then how to get the path
import os
full_path = os.path.join("C:/Users/bspay/PycharmProjects/PyATB4xLearning/src/september_2024/ex_10092024/example.txt")
file = open(full_path,'r')
content = file.read()
print(content)