import os

os.system('cls')

class Line:

    def __init__(self, a, b):
        self.a = {'x': a[0], 'y': a[1]}
        self.b = {'x': b[0], 'y': b[1]}

    def __str__(self):
        return f"Line: a=({self.a['x']},{self.a['y']}) b=({self.b['x']},{self.b['y']})"
    
    def length(self):
        return ((self.b['y'] - self.a['y']) ** 2 + (self.b['x'] - self.a['x']) ** 2) ** 0.5

    def slope(self):
        return (self.b['y'] - self.a['y']) / (self.b['x'] - self.a['x'])

line1 = Line((0,0), (3,3))
print(line1.length())
print(18 ** 0.5)
print(line1.slope())
print('_'*20)
line2 = Line((10,15), (3,3))
print(line2.length())
print(line2.slope())