from math import sqrt
x1 = input("Insert x1 value ")
y1 = input("Insert y1 value ")
x2 = input("Insert x2 value ")
y2 = input("Insert y2 value ")

final_x = (x2 - x1)**2 
final_y = (y2 - y1)**2
z = final_x + final_y 
print sqrt(z)
