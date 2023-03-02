# 3. Write a python program to find sum of product of corresponding even digits 
# of first any digit number and corresponding odd digit of any digit number 
# Such as n=1234 m=4567 output=4*7+2*5
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
temp1 = num1
temp2 = num2
sum = 0
while num1 > 0 and num2 > 0:
    firstNumDigit = num1 % 10
    secondNumDigit = num2 % 10
    if (firstNumDigit % 2 == 0 and secondNumDigit % 2 != 0):
        sum += firstNumDigit * secondNumDigit
    num1 = num1 // 10
    num2 = num2 // 10
print("Sum of product of corresponding even digits of first number %d and corressponding odd digit of second number %d is : %d" %(temp1, temp2, sum))