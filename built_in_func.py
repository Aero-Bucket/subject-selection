list_true=[1,2,3,4]
list_false=[0,0,1,2] # 0==empty==false
list_empty=[0,0,0,0]
print(all(list_true),all(list_false),all(list_empty)) 
print(any(list_true),any(list_false),any(list_empty))

non_ascii="Pythön is interesting"
print(ascii(non_ascii))

denary=5
binary=bin(denary)
print(binary)
print(binary.replace("0b",""))
print(format(denary,"b"))

num_barray=str(bytearray(denary)) # all null
list_barray=str(bytearray(list_true))
print(num_barray)
print(list_barray)
print(num_barray[12:-2])
print(list_barray[12:-2])

print(chr(97)) # ascii code of "a"

dict_num=dict([("x",1),("y",2)]) 
print(dict_num)

grocery=['bread', 'milk', 'butter']
print(list(enumerate(grocery)))
for count,item in enumerate(grocery,1):
    print(count,item)

list_denary=[0,1,2,3,4,5,6,7,8,9]
def even(x):
    if x%2 == 0:
        return x
    else:
        return None
list_filter1=list(filter(even,list_denary))
print(list_filter1)
list_filter2=list(filter(lambda x:x if x%2 == 0 else None,list_denary))
print(list_filter2)

list_map=list(map(lambda x:x**2,list_denary))

print(list_map)

