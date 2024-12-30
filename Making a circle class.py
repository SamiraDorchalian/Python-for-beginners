import os

os.system('cls')

#Class 👇

class Circle:
    pi = 3.14  #Class Attribute

    #our method 👇

    def __init__(self, r):
        self.r = r

    def calc_diameter(self):
        return self.r * 2

    def calc_area(self):
        # pi * (r **2)
        return self.pi * (self.r ** 2)
    
    def calc_circumferece(self):
        # 2 * pi * r
        return 2 * self.pi * self.r

# our objects 👇

circle1 = Circle(10)
print(circle1.calc_diameter())
print(circle1.calc_area())
print(circle1.calc_circumferece())

print('-'*20)

circle2 = Circle(10)
print(circle2.calc_area())
circle2.pi = 3.1415
print(circle2.calc_area())
print(circle2.calc_circumferece())