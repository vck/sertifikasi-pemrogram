class Student:
    def hello(self, name=None):
        if name is not None:
            print('Hey ' + name)
        else:
            print('Hey!')

# Creating a class instance
std = Student()

# Call the method
std.hello()

# Call the method and pass a parameter
std.hello('Vicky')