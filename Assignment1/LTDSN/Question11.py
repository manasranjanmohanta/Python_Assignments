# 11. WAP to do following using string
#  a) Check whether a string is palindrome or not
str = input("Enter a string: ") 
rev = reversed(str)
if(list(str) == list(rev)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


#  b) capitalize first and last character of each word in string
s = input("Enter a string: ")
str1 = list(s)
str1 +="\0"
for i in range(len(str1)):
    if(i == 0) or str1[i-1] == " ":
        str1[i] = str1[i].upper()
    else:
        if(str1[i] == " " or str1[i] == "\0"):
            str1[i-1] = str1[i-1].upper()
print("Your string is : ", "".join(str1))

#  c) categories the password as low medium and high
#  low – only numbers or alphabets and length less than 8
#  medium- number and alphabets and length more than 8
#  string- number, alphabet and special character should present 
# and length should be greater than 8
import re
password = input("Enter a password :")
if len(password) < 8 or password.isalpha() or password.isnumeric():
    print("Your password is strength is low")
elif len(password) >= 8 and (re.csearh('[a-zA-Z]', password)) and (re.search('[0-9]', password)):
    print("Your password is strength is medium")
elif len(password) >= 8 and (re.search('[a-zA-Z]', password)) and (re.search('[0-9]', password)) and (re.search('[^a-zA-Z0-9]', password)):
    print("Your password is strength is high")
else:
    print("Your password is invalid")
#  d) Find the letter used maximum and minimum time in a string
str = input("Enter a string: ")
freq = {}
for char in str:
    if char in freq:
        freq[char]  += 1
    else:
        freq[char] = 1
maxChar = max(freq, key = freq.get)
minChar = min(freq, key = freq.get)
print(" The letter user maximum time is :", maxChar)
print("The string used minimum time is :", minChar)

#  e) create a list to store unique character in string and another list 
# to store frequency of repeatation of unique character available in first list in the 
# string
str = input("Enter a string: ")
uniq = set(str)
freq = []
for i in uniq:
    count = str.count(i)
    freq.append(count)
print("Unique character: ",uniq)
print("Frequency: ",freq)

#  f) find and count number of words starts and ends with vowels in a
# string of multiple words
str = input("Enter a string: ")
list = str.split()
count = 0
result = []
for i in range(len(list)):
    if list[i].startswith("A") or list[i].startswith("E") or list[i].startswith("I") or list[i].startswith("O") or list[i].startswith("U") or list[i].startswith("a") or list[i].startswith("e") or list[i].startswith("i") or list[i].startswith("o") or list[i].startswith("u") and list[i].endswith("A") or list[i].endswith("E") or list[i].endswith("I") or list[i].endswith("O") or list[i].endswith("U") or list[i].endswith("a") or list[i].endswith("e") or list[i].endswith("i") or list[i].endswith("o") or list[i].endswith("u"):
        count += 1
        result.append(list[i])
print("The number of of word which are startswith and endswith vowel is :", count)
print("the words are: ",result)

#  g) create a list using names of 10 cities and pincodes. Combine 
# them all to convert it into string using join with delimiter “:”. Modify the names of 
# cities by adding state-cities in the string. Finally split it to have the information in 
# list in the format state-city-pincode
 # Define the list of cities and pincodes
cities_and_pincodes = [('Mumbai', 400001), ('Delhi', 110001), ('Bangalore', 560001), ('Chennai', 600001), ('Kolkata', 700001), ('Hyderabad', 500001), ('Ahmedabad', 380001), ('Pune', 411001), ('Jaipur', 302001), ('Lucknow', 226001)]

# Convert the list to a string with ":" delimiter
cities_and_pincodes_str = ":".join([f"{city}-{pincode}" for city, pincode in cities_and_pincodes])

# Define the mapping of cities to their respective states
state_mapping = {'Mumbai': 'Maharashtra', 'Delhi': 'Delhi', 'Bangalore': 'Karnataka', 'Chennai': 'Tamil Nadu', 'Kolkata': 'West Bengal', 'Hyderabad': 'Telangana', 'Ahmedabad': 'Gujarat', 'Pune': 'Maharashtra', 'Jaipur': 'Rajasthan', 'Lucknow': 'Uttar Pradesh'}

# Modify the city names to include their respective states
cities_and_pincodes_str = ":".join([f"{state_mapping[city]}-{city}-{pincode}" for city, pincode in cities_and_pincodes])

# Split the string to create a list in the format state-city-pincode
cities_and_pincodes_list = [city_pincode.split("-") for city_pincode in cities_and_pincodes_str.split(":")]

print(cities_and_pincodes_list)
