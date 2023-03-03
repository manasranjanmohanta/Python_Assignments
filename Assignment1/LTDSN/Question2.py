# 2. Write a python program to find total and average mark of a student and take 5
# different subject along with marks of 10 students using dictionary

# Create an empty dictionary to store the student information
student_marks = {}
for i in range(1, 2):
    # asking user to enter marks for 5 subjects
    subject1 = int (input("Enter mark of subject1:"))
    subject2 = int (input("Enter mark of subject2:"))
    subject3 = int (input("Enter mark of subject3:"))
    subject4 = int (input("Enter mark of subject4:"))
    subject5 = int (input("Enter mark of subject5:"))

    # calculate total marks and average marks for students
    total_marks = subject1 + subject2 + subject3 + subject4 + subject5
    
    average_marks = total_marks / 5

    student_marks[f"Student{i}"] = {
        "Subject1": subject1,
        "Subject2": subject2,
        "Subject3": subject3,
        "Subject4": subject4,
        "Subject5": subject5,
        "Total Marks": total_marks,
        "Average Marks": average_marks
    }
print(student_marks)
