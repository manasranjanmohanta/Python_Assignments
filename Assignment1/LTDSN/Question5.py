# 5. Write a Python program
# I. To add 'ing' at the end of a given string (length should be at least 
# 3). If the given string already ends with 'ing' then add 'ly' instead. If 
# the string length of the given string 5. is less than 3, leave it 
# unchanged. Sample String : 'abc' Expected Result : 'abcing' Sample 
# String : 'string' C 220.2 Expected Result : 'stringly'

str = input("Please enter a string : ")
if(len(str) >= 3):
    if(str.endswith("ing")):
        str += "ly"
    else:
        str += "ing"
print("The String is :", str)


# II. To get a string from a given string where all occurrences of its first 
# char have been changed to '$', except the first char itself.
str = input("Please enter a string :")
str1 = str[0]
str2 = str[1:]
str2 = str2.replace(str1, '$')
str = str1 + str2
print("The String is :", str)
