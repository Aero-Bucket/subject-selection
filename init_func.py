class add(object):

    def __init__(self,first_num,second_num):
        self.first_num=first_num
        self.second_num=second_num

    def add_func(self):
        print(self.first_num+self.second_num)

x=add(2,3)
x.add_func()



class minus(object):

    def arg_func(self,first_num,second_num):
        self.first_num=first_num
        self.second_num=second_num

    def minus_func(self):
        print(self.first_num-self.second_num)

y=minus()
y.arg_func(3,2)
y.minus_func()

