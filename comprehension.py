# plist=[x+y+z for x in "bg" for y in "bg" for z in "bg"]
# print(plist)

# counter=0

# for i in plist:
#     if list(i).count("b") == 1 and list(i).count("g") == 2:
#         counter+=1

# # print(counter)

# pdict={key:value for key,value in enumerate(plist,1)}
# print(pdict)

dup_list=[1,1,2,2,3,4,5,5,5,5]

def dedup(input_list):
    temp_set=set()
    temp_set.update(input_list)
    return list(temp_set)

print(dedup(dup_list))