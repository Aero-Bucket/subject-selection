input_money=int(input("Input amount of money> "))

def loop_money(lmoney):
    
    ltally=0

    while lmoney-1000 >= 0:
        lmoney-=1000
        ltally+=1

    while lmoney-500 >= 0:
        lmoney-=500
        ltally+=1

    while lmoney-100 >= 0:
        lmoney-=100
        ltally+=1

    while lmoney-50 >= 0:
        lmoney-=50
        ltally+=1

    while lmoney-20 >= 0:
        lmoney-=20
        ltally+=1

    while lmoney-10 >= 0:
        lmoney-=10
        ltally+=1

    while lmoney-5 >= 0:
        lmoney-=5
        ltally+=1

    while lmoney-2 >= 0:
        lmoney-=2
        ltally+=1

    while lmoney-1 >= 0:
        lmoney-=1
        ltally+=1

    while lmoney-0.5 >= 0:
        lmoney-=0.5
        ltally+=1

    while lmoney-0.2 >= 0:
        lmoney-=0.2
        ltally+=1

    while lmoney-0.1 >= 0:
        lmoney-=0.1
        ltally+=1

    print(f"You need {ltally} coin and cash")


def if_money(imoney):

    itally=0
    list_amount=[1000,500,100,50,20,10,5,2,1,0.5,0.2,0.1]

    for i in list_amount:
        while imoney-i >= 0:
            imoney-=i
            itally+=1

    print(f"You need {itally} coin and cash")

loop_money(input_money)
if_money(input_money)

