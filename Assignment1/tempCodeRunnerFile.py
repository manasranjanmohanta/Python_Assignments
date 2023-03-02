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
print(evenSum)
print(oddSum)
diff = evenSum - oddSum
print("Difference between Sum of product of consecutive even digits except 2 and 6 and Sum of product of consecutive odd digits except 3 and 7 is: ", diff)
