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


# IV. Sum of all prime digits
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    count = 0
    digit = int(num % 10)
    for i in range(1,digit + 1):
        if digit % i == 0:
            count += 1
    if count == 2:
        sum += digit
    num /= 10
print("Sum of all prime digits is: %i" % sum)

# V. Difference between average of all even digits except divisible by
# 4 and avearge of all odd digits except divisble by 3
num = int(input("Enter the number: "))
sumOfEvenDigits = 0
countOfEvenDigits = 0
sumOfOddDigits = 0
countOfOddDigits = 0
while num > 0:
    digit = int(num % 10)
    if digit % 2 == 0 and digit % 4 != 0: 
        sumOfEvenDigits += digit
        countOfEvenDigits += 1
    elif digit % 2 != 0 and digit % 3 != 0: 
        sumOfOddDigits += digit
        countOfOddDigits += 1
    num /= 10
averageOfEvenDigits = sumOfEvenDigits / countOfEvenDigits
averageOfOddDigits = sumOfOddDigits / countOfOddDigits
differenceofEvenOddDigits = averageOfEvenDigits - averageOfOddDigits
print("Difference between average of sum of all even digits except divisible by 4 and average of sum of all odd digits except divisible by divisible by 3: %i" % differenceofEvenOddDigits)



