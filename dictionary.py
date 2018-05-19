dict={1:"first",2:"second",3:"third"} # key:value

print("1st:",dict[1]) # print the value with the key '1'

print("\n")

for i in dict:
    print(i) # print the key
for i in dict:
    print(dict[i]) # print the value

print("\n")

del dict[3] # remove the value with the key '3'
for i in dict:
    print(dict[i])
