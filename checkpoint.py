import numpy as np

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'F'

# Step 2: Ask the user to enter the number of students and subjects
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Step 3: Create a Numpy array to store the marks of each student in each subject
marks_array = np.zeros((num_students, num_subjects))

# Step 4: Ask the user to enter the marks of each student in each subject
for i in range(num_students):
    for j in range(num_subjects):
        marks_array[i][j] = float(input(f"Enter marks for student {i+1} in subject {j+1}: "))

# Step 5: Calculate total marks for each student
total_marks = np.sum(marks_array, axis=1)

# Step 6: Calculate percentage for each student
percentage = (total_marks / (num_subjects * 100)) * 100

# Check if the percentage is within the valid range (0 to 100)
percentage = np.clip(percentage, 0, 100)

# Step 7: Calculate grade for each student
grades = [calculate_grade(percent) for percent in percentage]

# Step 8: Display the result in a tabular format
print("\nResult:")
print("{:<10} {:<15} {:<12} {:<6}".format("Student", "Total Marks", "Percentage", "Grade"))
for i in range(num_students):
    print("{:<10} {:<15} {:<12.2f} {:<6}".format(f"Student {i+1}", int(total_marks[i]), percentage[i], grades[i]))
