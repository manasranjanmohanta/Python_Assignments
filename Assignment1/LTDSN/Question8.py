# 8. Write a python program to find 1st,2nd and 3rd largest and smallest numbers in
# a list 20 user defined values
myList = []
print("Enter 20 numberes: ")
for x in range(0,20):
    myList.append(int(input()))
    x = x + 1
print("The List is : ", myList)
for i in range(len(myList)):
    for j in range(i+1,len(myList)):
        if myList[i] > myList[j]:
            temp = myList[i]
            myList[i] = myList[j]
            myList[j] = temp

    i = i + 1
print("After sorting the list is :", myList)
print("The 1st largest number in list is :", myList[len(myList)-1])
print("The 2nd largest number in list is :", myList[len(myList)-2])
print("The 3rd largest number in list is :", myList[len(myList)-3])
print("The smallest number in list is :", myList[0])       
    