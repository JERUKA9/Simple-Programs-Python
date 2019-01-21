import os

list = os.listdir("..")

path="files/00/data.txt"

dir_path=os.path.dirname(path)

os.makedirs(dir_path)

print(list)

open(path,"+w").close()
