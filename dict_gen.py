key=input("Input keys here, use comma to separate: ").split(",")
value=input("Input values here, use comma to separate: ").split(",")
dictionary={}

if len(key)==len(value):
    for i in range(len(key)):
        dictionary[key[i]]=value[i]
elif len(key)>=len(value):
    print("Not enough values")
else:
    print("Not enough keys")

for a,b in dictionary.items():
    print(f"{a} corresponds to {b}")
