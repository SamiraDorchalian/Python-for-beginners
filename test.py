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

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        return self.firstname.title() + ' ' + self.lastname.title()


class Student(Person):
    def __init__(self, firstname, lastname, major, university):
        super().__init__(firstname, lastname)
        self.major = major
        self.university = university

    def fullname(self):
        return f'{self.firstname} {self.lastname}. I am studing {self.major}'
    
    def education_info(self):
        return f'{self.university}: {self.major} '


class Teacher(Person):
    def __init__(self, firstname, lastname, university, department):
        super().__init__(firstname, lastname)
        self.university = university
        self.department = department
    
    def working_info(self):
        return f'I am working in {self.university} at {self.department} department.'



samira_stu = Student('samira', 'dorchalian' , 'Computer Engineering', 'Azad')
print(samira_stu.fullname())

arezoo_teacher = Teacher('Arezoo', 'dorchalian', 'Azad', 'Math')
print(arezoo_teacher.fullname())