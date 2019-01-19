f = open("file.txt","w+")

f.write("numbers 1234567890\n ")

print(f.read(3))

f.seek(4)

print(f.readlines())





f.close()

