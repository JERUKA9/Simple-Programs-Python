try:
    file=open("text.txt","w+")
    file.write("numbers 1234567890")
    file.close()
    
except:
    FileNotFoundError
    