# 1. Write a python program to find following using looping and decision making 
# without function
# I. Sum of all digits of any numbers
num = int(input("Enter a number: "))
sum = 0
while num != 0:
    sum += int(num % 10)
    num /= 10
print("Sum of all digits is: %i" % sum)


# II. Sum of all even digits of any number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = int(num % 10)
    if digit % 2 == 0:
        sum += digit
    num /= 10
print("Sum of all even digits is: %i" % sum)


# III. Sum of all odd digits of any number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = int(num % 10)
    if digit  % 2 != 0:
        sum += digit
    num /= 10
print("Sum of all odd digits is: %i" % sum)


