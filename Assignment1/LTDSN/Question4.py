# 4. Write a Python program to print and store ‘n terms of Fibonacci series in list
n = int(input("Enter the number of of terms to print:"))
fib1 = 0
fib2 = 1
fibonacci_list = [fib1, fib2]
for i in range(2, n):
    fib = fib1 + fib2
    fibonacci_list.append(fib)
    fib1 = fib2
    fib2 = fib
print(fibonacci_list)
