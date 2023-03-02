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