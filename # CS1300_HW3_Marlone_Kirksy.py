# CS1300_HW3_Marlone_Kirksy.py


# Problem 1: Boolean Expression Evaluator


print("Problem 1: Boolean Expression Evaluator")

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

expr1 = a < b < c
expr2 = not (a > b or b > c)
expr3 = a <= b and b <= c

print("a < b < c :", expr1)
print("not (a > b or b > c) :", expr2)
print("a <= b and b <= c :", expr3)

if expr2 == expr3:
    print("De Morgan's confirmed: Expressions 2 and 3 match!")
else:
    print("Expressions do not match.")

print()



# Problem 2: Weather


print("Problem 2: Weather Advisory System")

temp = int(input("Enter temperature: "))
rain = input("Is it raining? (yes/no): ")

if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temp > 85:
    if rain == "yes":
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif temp >= 60:
    if rain == "yes":
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif temp >= 32:
    print("It's cold — bundle up!")

else:
    print("FREEZE WARNING: Roads may be icy!")

print()



# Problem 3: Student Grade Report


print("Problem 3: Student Grade Report")

name = input("Enter student name: ")

exam1 = float(input("Enter Exam 1 score: "))
exam2 = float(input("Enter Exam 2 score: "))
exam3 = float(input("Enter Exam 3 score: "))

average = (exam1 + exam2 + exam3) / 3

if average >= 90:
    grade = "A"
elif average >= 87:
    grade = "A-"
elif average >= 83:
    grade = "B+"
elif average >= 80:
    grade = "B"
elif average >= 77:
    grade = "B-"
elif average >= 73:
    grade = "C+"
elif average >= 70:
    grade = "C"
elif average >= 67:
    grade = "C-"
elif average >= 63:
    grade = "D+"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

if average >= 90:
    status = "Dean's List"
elif average >= 70:
    status = "Good Standing"
elif average >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

print("============================")
print(" STUDENT GRADE REPORT")
print("============================")
print("Student:", name)
print("Exam 1:", exam1)
print("Exam 2:", exam2)
print("Exam 3:", exam3)
print("----------------------------")
print("Average:", round(average, 2))
print("Grade:", grade)
print("Status:", status)
print("============================")