filename=input("filename> ")
newfile=open(f"new_{filename}","w")
print(filename)

with open(filename,"r") as f:
    for line in f:
        newfile.write(line.replace("    ","\t"))

