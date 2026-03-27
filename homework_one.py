# Ask the user for student information
first_name = input("Enter the student's first name: ")
last_name = input("Enter the student's last name: ")

# Ask the user for exam scores and convert them to floats
exam_score1 = float(input("Enter the first exam score: "))
exam_score2 = float(input("Enter the second exam score: "))
exam_score3 = float(input("Enter the third exam score: "))

# Calculate average score
average_score = (exam_score1 + exam_score2 + exam_score3) / 3

# Print the results
print(f"\nStudent: {first_name} {last_name}")
print(f"Average exam score: {average_score:.1f}")