#Encapsulation is the process of wrapping data and methods that 
# work on that data within one unit. This puts restrictions 
# on accessing variables and methods directly and can prevent
#  the accidental modification of data. To prevent accidental change, 
# an object’s variable can only be changed by an object’s method. 
# This is called encapsulation.

class student:
    def __init__(self, name, age):
        self.__name = name  # private variable
        self.__age = age    # private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

#Inheritance is the process by which one class takes 
# on the attributes and methods of another class.

class parent:
    def __init__(self, name):
        self.name = name

class child(parent):
    def show(self):
        print(f"Child's parent name is: {self.name}")
child1 = child("sunita")
child1.show()