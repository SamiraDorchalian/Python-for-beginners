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


# import sys

# from termcolor import colored, cprint

# text = colored("Hello, World!", "red", attrs=[ "blink"])
# print(text)
# cprint("Hello, World!", "green", "on_red")

# print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
# print_red_on_cyan("Hello, World!")
# print_red_on_cyan("Hello, Universe!")

# for i in range(10):
#     cprint(i, "magenta", end=" ")

# cprint("Attention!", "yellow", attrs=["underline"], file=sys.stderr)

#-----------------------------------------------#
# Exception Handling & use raise

# def calc_income(income):
#     if income < 0:
#         raise Exception('Income should not be a negetive number!')

#     print('first')
#     return income * 2

# user_income = int(input('Enter your income: '))

# try:
#     print(calc_income(user_income))
# except:
#     print('EXCEPTION')

# print('second')

#-----------------------------------------------#
# Exception Handling & use raise & assert


# def calc_income(income):
#     assert income >= 0, 'Income should not be a negetive number!'

#     print('first')
#     return income * 2

# user_income = int(input('Enter your income: '))

# try:
#     print(calc_income(user_income))
# except:
#     print('EXCEPTION')

# print('second')

#-----------------------------------------------#
# Exception Handling & use raise & assert - else - finally

# a = 10
# b = int(input('Enter a number: '))

# try:
#     b = c + 10    
#     # print(b)

# except ZeroDivisionError:
#     print('Exception!')
# except ModuleNotFoundError:
#     print('another expetion!')
# # except Exception:
# #     print('some other error')
# else:
#     print('ELSE')
# finally:
#     print('Finaly')

#-----------------------------------------------#
#Exception Handling
# Creating arbitrary errors with the help of inheritance

# class NegetiveIncomeError(Exception):
#     pass

# class  NegetiveAgeError(Exception):
#     def __init__(self, message, age):
#         self.message = message
#         self.age = age

# def check_age(age):
#     if age < 0:
#         raise NegetiveAgeError(f'Your age ({age}) can not be negetive.', age)
#     return age * 2 

# def check_income(num):
#     if num < 0:
#         raise NegetiveIncomeError('You income can not be negetive.')

#     return num

# # user_income = int(input('Enter your income: '))
# # check_income(user_income)

# user_age = int(input('Enter your age: '))

# try:
#     check_age(user_age)
# except NegetiveAgeError as e:
#     print(e.message, e.age)

#-----------------------------------------------#
#Exception Handling

# result = None

# while True:
#     user_input = input('Enter your number: ')

#     try:
#         result = int(user_input)
#         break
#     except ValueError:
#         try:
#             result = float(user_input)
#             break
#         except ValueError:
#             print('You have to enter a number. Please try again.')

# print(type(result))
# print(f'Result: {result}')

#-----------------------------------------------#
#Controlling files in Python
# w: write, r: read, a: append

#--------------------------
#write
#file = open('names.txt', 'w')

# file.write('samira\nDorchalian\n1998')
#---or---writelines------------
# file = open('names.txt', 'w')
# file.write('hello')
# file.writelines(['samira', 'dorchalian', 'developer'])
#--------------------------
# names = ['samira', 'dorchalian', '26']
#---description-----------------------
# if we don't put \n in last our words , Words stick together.
# so we can fixed with map & fun lambda or use write & join
#--------------------------
# file.writelines(map(lambda name: name+'\n', names))
# file.write('\n'.join(names))

#--------------------------
# read from another file
# file = open('names.txt', 'r')
# # a = file.read()
# # print(a.split('\n'))
# # for line in a.split('\n'):
# #     print(f'Hello {line.title()}')
# # ---or---readlines()---------
# # print(file.readlines())
# # ---or---readline()----------
# while True:
#     line = file.readline()
#     print(line, end='')
#     if line == '':
#         break

# print('END')
#---Coding practice-----------------------
# names_file = open('names.txt', 'r')

# names = names_file.read()
# names = names.split('\n')
# print(names)

# while True:
#     user_input = input('Enter name: ')
#     if user_input == 'exit':
#         break
#     names.append(user_input)
#     print(names)

#-----------------------------------------------#
#close and how to close files
#useing with

# names_file = open('names.txt', 'r')

# try:
#     names = names_file.read()
    
#     names = names.split('\n')

#     print(names)

#     while True:
#         user_input = input('Enter name: ')
#         if user_input == 'exit':
#             break
#         names.append(user_input)
#         print(names)
# finally:
#     names_file.close()

#-----------------------------------------------#
#useing with
# names = []

# with open('names.txt', 'r') as reader:
#     # print(reader.read())
#     for line in reader.read().split('\n'):
#         names.append(line)
#     print('something')

# print(names)
# print('END')

#-----------------------------------------------#
#append
# f = open('names.txt', 'a')

# f.write('another line')
#---with, whit-----------

# with open('names.txt', 'a')as names_file:
#    names_file.write('\nThis is new')

#-----------------------------------------------#
#Package TKinter

# import tkinter as tk
# # from tkinter import LEFT, BOTTOM

# window = tk.Tk()
#---Button-------------------

# def button_clicked():
#     print('Clicked!')
#---or we can use lambda----------
# button = tk.Button(
#     master=window,
#     text='Click me!',
#     # command=button_clicked,
#     command=lambda: print('Clicked me is run')
# )
# button.pack()
#---StringVar--------------
# text_var = tk.StringVar()
#---Label-------------------
# import tkinter as tk
# window = tk.Tk()

# text1 = tk.Label(
#     master = window, 
#     # text = 'Welcome',
#     textvariable=text_var,
# )
# first_name = tk.Label(
#     master = window, 
#     text = 'Samira',
# )
# last_name = tk.Label(
#     master = window, 
#     text = 'Dorchalian',
# )
# name_text = tk.Label(
#     window,
#     text='First Name: ',
# )
# first_name.pack()
# last_name.pack()

# window.mainloop()
#---Input Entry----------------
#---Contact Lable & Entry together with class StringVar----------------

# import tkinter as tk
# # from tkinter import LEFT, BOTTOM
# window = tk.Tk()

# user_input = tk.Entry(
#     window,
#     textvariable=text_var
# )
# name_text.pack(side=LEFT)
# user_input.pack(side=LEFT)
# text1.pack(side=LEFT)

# window.mainloop()
#----------
# import tkinter as tk

# window = tk.Tk()

# name_entry = tk.Entry(
#     window,
# )
# show_name_label = tk.Label(
#     window,
# )
# def button_clicked():
#     # print(name_entry.get())
#     show_name_label['text'] = name_entry.get()

# submit_button = tk.Button(
#     window,
#     text='Submit',
#     # command=lambda: print('clicked! ')
#     command=button_clicked,
# )


# name_entry.pack()
# submit_button.pack()
# show_name_label.pack()

# window.mainloop()

#----------
import tkinter as tk
from tkinter import E, W, N, S

window = tk.Tk()

label_title = tk.Label(
    window,
    text='Enter your data',
)
label_title.grid(row=0, column=0, columnspan=2)

label_input_name = tk.Label(
    window,
    text='First Name: ',
)
entry_name = tk.Entry(
    window,
    width=10,
)
label_input_name.grid(row=1,column=0, sticky=(W, ))
entry_name.grid(row=1, column=1, sticky=(W, ))
#-------------
label_input_last_name = tk.Label(
    window,
    text='Last Name: ',
    height=3,
)
entry_last_name = tk.Entry(
    window,
)
label_input_last_name.grid(row=2,column=0, sticky=(W, ))
entry_last_name.grid(row=2, column=1, sticky=(N, S))
#-------------
label_age = tk.Label(
    window,
    text='age: '
)
entry_age = tk.Entry(
    window,
    width=10,
)
label_age.grid(row=3,column=0, sticky=(W, ))
entry_age.grid(row=3,column=1, sticky=(W, ))
#-------------
submit_button = tk.Button(
    window,
    text='Submit',
)
submit_button.grid(row=4,column=0, columnspan=2,sticky='ew') #ew => east & west
# submit_button.grid(row=4,column=1, sticky='ew') 
submit_button.grid(row=4,column=1, sticky=(E, W)) # import E= east-e & W= west-w from tkinter for using default sticky like tuple
#north
#east
#west
#south
window.mainloop()