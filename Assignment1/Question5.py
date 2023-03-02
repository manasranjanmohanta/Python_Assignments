# 5. Write a python program compute following series and take a numbers num 
# as input x-x3/3! + x5/5!-x7/7!+------+xn/n!where x=sum of all even digits except 2 
# and 8 and n= sum of all odd digits except 1 and 3
num = int(input("Enter a number:"))
evenSum = 0
oddSum = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        if digit != 2 and digit != 8:
            evenSum += digit
    else:
        if digit != 1 and digit != 3:
            oddSum += digit
    num = num // 10       
x = evenSum
n = oddSum
sum = x
bool = False
def factorial(x):
    fact = 1
    while x > 0:
        fact = fact * x
        x = x - 1
    return fact
for i in range(3,n+1):
    term = pow(x, i) / factorial(i)
    if (i % 2) != 0:
        if(bool):
            sum = sum + term
            bool = False
        else:
            sum = sum - term
            bool = True
print("%.5f" %sum)