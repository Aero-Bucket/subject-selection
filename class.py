class MyClass(object):

    instance_var=10

    def instance_method(self):
        return "instance method",self.instance_var
        # "self" refers to the INSTANCE
        # this will use the instance_var in the INSTANCE

    @classmethod
    def class_method(cls):
        return "class method",cls.instance_var
        # "cls" refers to the CLASS
        # this will use the instance_var in the CLASS

    @staticmethod
    def static_method(num):
        return "static method",num
        # cannot access things in the instance

x=MyClass()
x.instance_var=20
print(x.instance_method())

y=MyClass()
y.instance_var=30
print(y.instance_method())
# instance_var in different instance are different


print(MyClass.class_method())
print(MyClass.static_method(40))
# don't need to create a instance in order to access the method


class Person(object):
    
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

    # factory method 
    @classmethod
    def parse(cls,name):
        name1,name2=name.split()
        return cls(name1,name2)

    def hello(self):
        return f"Hello {self.name}, {self.surname*3}!"

# inheritance
class Man(Person):
    pass

m=Man.parse("henry ho")
print(m.hello())
