class Param_test(object):

    def print_num(self,parameter=None):

        if parameter != None:
            number=parameter
        else:
            number=10

        print(number)

x=Param_test()
x.print_num()
x.print_num(20)
