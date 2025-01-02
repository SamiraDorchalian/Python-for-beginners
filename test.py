import os
os.system('cls')

#-----------------------------------------------#

# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#     def print_details(self):
#         return f'Color : {self.color} , Model : {self.model}'
    
# car1 = Car('blue' , 'BMW')
# car2 = Car('yellow', 'ferary')
# car3 = Car('red', 'Samand')

# print( car1 , car2, car3)
# print(car1.print_details())
# print(car2.print_details())
# print(car3.print_details())

#-----------------------------------------------#

# class House:

#     country = 'iren'
#     x = 123

#     def __init__(self, color, num_of_room, a):
#         self.color = color
#         self.num_of_room = num_of_room
#         self.a = a
#     def house_description(self):
#         return (self.color, self.num_of_room, self.a)

# house1 = House('blue', 4 , 100)

# print(house1)
# print(house1.country)
# house1.country = 'USA'
# print(house1.country)
# del house1.country
# print(house1.country)

#-----------------------------------------------#

#Inheritance

# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def fullname(self):
#         return self.firstname.title() + ' ' + self.lastname.title()

# class Student(Person):
#     def __init__(self, firstname, lastname, major, university):
#         super().__init__(firstname, lastname)
#         self.major = major
#         self.university = university

#     def fullname(self):
#         return f'{self.firstname} {self.lastname}. I am studing {self.major}'
    
#     def education_info(self):
#         return f'{self.university}: {self.major} '

# class Teacher(Person):
#     def __init__(self, firstname, lastname, university, department):
#         super().__init__(firstname, lastname)
#         self.university = university
#         self.department = department
    
#     def working_info(self):
#         return f'I am working in {self.university} at {self.department} department.'

# samira_stu = Student('samira', 'dorchalian' , 'Computer Engineering', 'Azad')
# print(samira_stu.fullname())

# arezoo_teacher = Teacher('Arezoo', 'dorchalian', 'Azad', 'Math')
# print(arezoo_teacher.fullname())

#-----------------------------------------------#

# Polymorphism in object orientation

# class Shape: #Abstrack Class

#     pi = 3.14

#     def __init__(self, kind, name):
#         self.kind = kind
#         self.name = name

#     def area(self):
#         raise NotImplementedError('All children of Shape class should redefind the area method')

# class Circle(Shape):
#     def __init__(self, kind, name, r):
#         super().__init__(kind, name)
#         self.radius = r

#     def area(self): # OverRide
#         return self.pi * (self.radius ** 2)

# class Square(Shape):
#     def __init__(self, kind, name, side_length):
#         super().__init__(kind, name)
#         self.side_length = side_length

#     def area(self): # OverRide
#         return self.side_length ** 2

# def show_area(s):
#     print(s.area())

# square1 = Square('square', 'a', 10)
# circle1 = Circle('circle', 'b', 10)
# circle2 = Circle('circle', 'c', 4)
# # print(square.area())
# # print(circle.area())

# # show_area(square)
# # show_area(circle)

# for shape in [square1, circle1, circle2]:
#     show_area(shape)

#-----------------------------------------------#

# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading.

# class complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#      # adding two objects 
#     def __add__(self, other):
#         # return self.a + other.a, self.b + other.b
#         a = self.a + other.a
#         b = self.b + other.b
#         return complex(a, b)
    
#     def __str__(self):
#         return f'{self.a}, {self.b}'

# ob1 = complex(1, 2)
# ob2 = complex(2, 3)
# ob3 = ob1 + ob2
# print(ob3)

#-----------------------------------------------#

# print(dir(0))

#-----------------------------------------------#


# class A(object):
#     def __eq__(self, other):
#         print("A __eq__ called: %r == %r ?" % (self, other))
#         return self.value == other
# class B(object):
#     def __eq__(self, other):
#         print("B __eq__ called: %r == %r ?" % (self, other))
#         return self.value == other   

# a = A()
# a.value = 3
# b = B()
# b.value = 4
# a == b

#-----------------------------------------------#
### Installation and use of ready-made packages


import sys

from termcolor import colored, cprint

text = colored("Hello, World!", "red", attrs=[ "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
    cprint(i, "magenta", end=" ")

cprint("Attention!", "yellow", attrs=["underline"], file=sys.stderr)