# 3. Write a python program to store details of a student like rollno, regdno, 
# name, branch, stream, sem, phone no,address in dictionary and print the 
# details in cv format

# create an empty dictionary to store details of a student
student_info = {}
rollno = int(input("Enter rollno: "))
regdno = int(input("Enter regdno: "))
name = input("Enter name: ")
branch = input("Enter branch: ")
stream = input("Enter stream: ")
sem = input("Enter sem: ")
phone_no = input("Enter phone no: ")
address = input("Enter address: ")

student_info = {
    "rollno": rollno,
    "regdno": regdno,
    "name": name,
    "branch": branch,
    "stream": stream,
    "sem": sem,
    "phone_no": phone_no,
    "address": address
}

print("CV FORMAT")
print("Roll No : " + student_info[rollno])
print("Regd No : " + student_info[regdno])
print("Name : " + student_info[name])
print("Branch : " + student_info[branch])
print("Stream : " + student_info[stream])
print("Semester : " + student_info[sem])
print("Phone No : " + student_info[phone_no])
print("Address : " + student_info[address])


