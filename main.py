import math
import numpy
#1
a = 1
b = -1000
c = 1
#2 +
# a = 6
# b = 5
# c = -4
#3 +
# a = 6*pow(10, 30)
# b = 5*pow(10, 30)
# c = -4*pow(10, 30)
#4 +
# a = pow(10, -30)
# b = -pow(10, 30)
# c = pow(10, 30)
#5 +
# a = 1.0000000
# b = -4.0000000
# c = 3.9999999


d = b*b - 4*a*c
x1 = (-b+math.sqrt(d))/(2*a)
x2 = (-b-math.sqrt(d))/(2*a)

x12 = (-b+numpy.sign(b)*math.sqrt(d))/(2*a)
x22 = c/(x1*a)

if (x2 > x22):
    print("x1: " + str(x1) + "   x2: " + str(x2))
else:
    print("x1: " + str(x1) + " x2: " + str(x22))
