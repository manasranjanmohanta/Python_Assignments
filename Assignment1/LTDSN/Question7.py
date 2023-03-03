# 7. Write a python program to find difference between average of all even 
# numbers except divisible by 4 and average of all odd numbers except 
# divisible by 5 in a list of user defined 20 values?
list = []
print("Enter 20 numbers : ")
for i in range(20):
   list.append(int(input()))
evenSum = oddSum = 0
evenCount = oddCount = 0
for i in list:
   if i % 2 == 0:
      if i % 4 != 0:
         evenSum += i
         evenCount += 1
   else:
      if i % 5 != 0:
         oddSum += i
         oddCount += 1
avgOfEven = evenSum / evenCount
avgOfOdd = oddSum / oddCount
diff = avgOfEven - avgOfOdd
print("The list is : ",list)
print("average of all even numbers except divisible by 4 and average of all odd numbers except divisible by 5 is : ", diff)