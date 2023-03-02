# 4. Write a python program to compute following series and take input x and n
# I. 1-x2/2! + x3/3!-x4/4!+------+xn/n!
x = int(input("Enter the value of the x: "))
n = int(input("Enter the value of the n: "))
sum = 0
def factorial(x):
    fact = 1
    while x > 0:
        fact = fact * x
        x = x - 1
    return fact
for i in range(2,n+1):
    term = pow(x, i) / factorial(i)
    if (i % 2) == 0:
        sum = sum + term
    else:
        sum = sum - term
print("%.5f" %sum)


# II. x-x3/3! + x5/5!-x7/7!+------+xn/n!
x = int(input("Enter the value of the x: "))
n = int(input("Enter the value of the n: "))
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


# III. 1+x2/2! + x4/4!+x6/6!+------+xn/n!
x = int(input("Enter the value of the x: "))
n = int(input("Enter the value of the n: "))
sum = 1
def factorial(x):
    fact = 1
    while x > 0:
        fact = fact * x
        x = x - 1
    return fact
for i in range(2,n+1):
    term = pow(x, i) / factorial(i)
    if (i % 2) == 0:
        sum = sum + term
print("%.5f" %sum)


# IV. x-x3/3! + x5/5!-x7/7!+x11/11!------+xn/n!
x = int(input("Enter the value of the x: "))
n = int(input("Enter the value of the n: "))
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

