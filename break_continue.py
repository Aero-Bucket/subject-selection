test_list=[1,2,3,4]

for i in test_list:
    if i==3:
        break # stop the loop when i=3
    print(i)

print("\n")

for i in test_list:
    if i==3:
        continue # skip i when i=3
    print(i)
