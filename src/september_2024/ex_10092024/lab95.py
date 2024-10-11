import os

#operating system -work with files,path related to OS

print(os.name)

if os.name == 'nt':
    print("using window")
else:
    print("no windows")

print(os.getcwd())
os.mkdir("payal_dir")

#will use in future
full_path = os.path.join('folder','file.txt')
print(full_path)