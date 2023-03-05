# 10.Write a python program to create a tuple of constants values like pi and 
# exponent and use them to find area and perimeter of circle?
import math

# create a tuple of constants values
constant = (math.pi, math.e)

# take user input for the radius of the circle
radius = float(input("Enter radius of the circle: "))

# calculate the area and perimeter of the circle using constant values
area = constant[0] * radius * radius
perimeter = 2 * constant[0] * radius

# print the result
print("The area of circle is : " , area)
print("The perimeter of circle is : " , perimeter)

