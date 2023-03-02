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
    digit = int(num % 10)
    if (digit == 2 or digit == 3 or digit == 5 or digit ==7):
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


# VI. Find kth digit from frontside or back side of any digits number 
# and find its poistional value
num = int(input("Enter a number: "))
k = int(input("Enter a positional value: "))
l = k
num1 = num2 = num
rev = count = 0
while num1 > 0:
    digit = int(num1 % 10)
    rev  = rev * 10 + digit
    count += 1
    num1 = num1 // 10
x = 1
y = int(pow(10,count - 1))
while k > 0:
    backSideNumber = num2 % 10
    backSidePos = backSideNumber * x 
    x = x * 10
    num2 = num // 10
    frontSideNumber = rev % 10
    frontSidePos = frontSideNumber * y
    y = y // 10
    rev = rev // 10
    k = k - 1
print("%ith digit from front side of %i is : %i" % (l,num,frontSidePos))
print("%ith digit from front side of %i is : %i" % (l,num,backSidePos))


# VII. Sum of product of consecutive digits of any digit number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit1 = num % 10
    digit2 = (num // 10) % 10
    sum += (digit1 * digit2)
    num = num // 10
print("Sum of product of consecutive digits is : ", sum)


# VIII. Sum of product of consecutive even digits of any digit number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit1 = num % 10
    digit2 = (num // 10) % 10
    if (digit1 % 2 == 0 and digit2 % 2 == 0):
        sum += (digit1 * digit2)
    num = num // 10
print("Sum of product of consecutive even digits is: ", sum)


# IX. Sum of product of consecutive odd digits of any digit number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit1 = num % 10
    digit2 = (num // 10) % 10
    if (digit1 % 2 != 0 and digit2 % 2 != 0):
        sum += (digit1 * digit2)
    num = num // 10
print("Sum of product of consecutive odd digits is: ", sum)


# X. Sum of product of consecutive prime digits of any digit number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit1 = num % 10
    digit2 = (num // 10) % 10
    if (digit1 == 2 or digit1 == 3 or digit1 == 5 or digit1 == 7) and ( digit2 == 2 or digit2== 3 or digit2 == 5 or digit2 == 7):
        sum += (digit1 * digit2)
    num = num // 10
print("Sum of product of consecutive odd digits is: ", sum)


# XI. Difference between Sum of product of consecutive even digits 
# except 2 and 6 and Sum of product of consecutive odd digits 
# except 3 and 7 of any digit number
num = int(input("Enter a number: "))
evenSum= 0
oddSum= 0
while num > 0:
    digit1 = num % 10
    digit2 = (num // 10) % 10
    if (digit1 % 2 != 0 and digit2 % 2 != 0):
        if digit1 != 3 and digit2 != 7:
            oddSum += (digit1 * digit2)
    elif (digit1 % 2 == 0 and digit2 % 2 == 0):
        if(digit1 != 2 and digit2 != 6):
            evenSum += (digit1 * digit2)
    num = num // 10
diff = evenSum - oddSum
print("Difference between Sum of product of consecutive even digits except 2 and 6 and Sum of product of consecutive odd digits except 3 and 7 is: ", diff)



