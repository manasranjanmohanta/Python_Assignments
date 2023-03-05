# 9. Write a python program to find repeated numbers as well as frequency of 
# repetition of numbers in a list of 20 user defined values?
myList = [2, 5, 2, 6, 5, 3, 4]
mySet = set(myList)
newList = []
for i in mySet:
    count = myList.count(i)
    newList.append(count)
print("Given list is : ", myList)
print("Unique item in the list is : ", mySet)
templist = list(mySet)
myDict = {}
for i in range(len(templist)):
    myDict[templist[i]] = newList[i]
    i = i + 1
print(myDict)