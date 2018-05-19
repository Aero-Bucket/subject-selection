def fibonacci(iterations):
    a,b=0,1
    for i in range(iterations):
        print(a)
        a,b=b,a+b

fibonacci(int(input("Amount? ")))
