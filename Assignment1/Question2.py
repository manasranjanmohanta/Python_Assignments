# 2. Write a python program to find sum of product of corresponding digits of two 
# any digit number Such as n=1234 m=7896 output=6*4+9*3+8*2+7*1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
temp1 = num1
temp2 = num2
sum = 0
while num1 > 0 and num2 > 0:
    firstNumDigit = num1 % 10
    secondNumDigit = num2 % 10
    sum += firstNumDigit * secondNumDigit
    num1 = num1 // 10
    num2 = num2 // 10
print("Sum of product of corresponding digits of two numbers %d and %d is : %d" %(temp1, temp2, sum))

