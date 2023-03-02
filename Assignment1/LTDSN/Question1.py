# 1. Write a python program to create a list of prime numbers as per given range
num = int(input("Enter a range of prime numbers: "))
primeNumbers = []
for x in range(2,num):
    isPrime = True
    for i in range(2,x):
        if x % i == 0:
            isPrime = False
    if isPrime:
        primeNumbers.append(x)
print("list of prime numbers: ", primeNumbers)