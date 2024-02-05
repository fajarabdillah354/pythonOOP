class Person:
    def __init__(self, input_name, input_class):
        self.__name = input_name
        self.__class = input_class

    def getting_name(self):
        print("your name is : ",self.__name)
        
    
    def setter(self, input_nama):
        print("enter your name : ")
        self.__name = input(str(input_nama))

    def getting_class(self):
        print("your class is : ", self.__class)

    def setter_class(self, input):
        print("your class is : ")
        self.__class = input(int(input))

orang1 = Person("fajar",3)
orang1.getting_name()
orang1.setter("ujeh")
    
