# 1. Write a python program to find following using looping and decision making 
# without function
# I. Sum of all digits of any numbers
num = int(input("Enter a number: "))
sum = 0
while num != 0:
    sum += int(num % 10)
    num /= 10
print("Sum of all digits is: %i" % sum)


