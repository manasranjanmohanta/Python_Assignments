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
