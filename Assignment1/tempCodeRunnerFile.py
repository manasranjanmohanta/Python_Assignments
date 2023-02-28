num = int(input("Enter a number: "))
sum = 0
count = 0
while num > 0:
    digit = int(num % 10)
    for i in range(1,digit + 1):
        if digit % i == 0:
            count += 1
    if count == 2:
        sum += digit
    num /= 10
print("Sum of all odd digits is: %i" % sum)