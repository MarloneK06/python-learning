"""
Student Grade Tracker
CS 1300 — Lecture 5 Mini-Project

A modular program that collects exam scores,
calculates a letter grade and academic standing,
displays a formatted report, and includes tests.
"""

def get_student_name():
    """Prompt for and return the student's name."""
    name = input("Student name: ")
    return name


def is_valid_score(score):
    """Return True if score is between 0 and 100."""
    return score >= 0 and score <= 100


def get_validated_score(prompt):
    """Keep asking for a score until the user enters a valid one."""
    while True:
        score = int(input(prompt))

        if is_valid_score(score):
            return score
        else:
            print("Invalid score. Enter a number from 0 to 100.")


def get_exam_scores(num_exams):
    """Collect and return a list of exam scores."""
    scores = []

    for i in range(num_exams):
        score = get_validated_score(f"Exam {i + 1} score: ")
        scores.append(score)

    return scores


def calculate_average(scores):
    """Return the average of a list of scores."""
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


def determine_letter_grade(average):
    """Return the letter grade based on the average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def determine_standing(average):
    """Return academic standing based on the average."""
    if average >= 90:
        return "Dean's List"
    elif average >= 70:
        return "Good Standing"
    elif average >= 60:
        return "Academic Probation"
    else:
        return "Academic Warning"


def print_divider(symbol="=", length=30):
    """Print a divider line."""
    print(symbol * length)


def display_report(name, scores, average, grade, standing):
    """Display the student grade report."""
    print_divider()
    print("STUDENT GRADE REPORT")
    print_divider()

    print(f"Student: {name}")

    for i in range(len(scores)):
        print(f" Exam {i + 1}: {scores[i]}")

    print_divider("-", 30)
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    print_divider()


def test_grade_tracker():
    """Run tests for the grade tracker functions."""
    print("Running tests...")

    # Test is_valid_score
    if is_valid_score(90) == True:
        print("PASS: valid score")
    else:
        print("FAIL: valid score")

    if is_valid_score(-5) == False:
        print("PASS: negative score")
    else:
        print("FAIL: negative score")

    if is_valid_score(101) == False:
        print("PASS: score over 100")
    else:
        print("FAIL: score over 100")

    # Test calculate_average
    if calculate_average([90, 80, 70]) == 80:
        print("PASS: average normal")
    else:
        print("FAIL: average normal")

    if calculate_average([]) == 0:
        print("PASS: average empty list")
    else:
        print("FAIL: average empty list")

    # Test determine_letter_grade
    if determine_letter_grade(95) == "A":
        print("PASS: grade A")
    else:
        print("FAIL: grade A")

    if determine_letter_grade(85) == "B":
        print("PASS: grade B")
    else:
        print("FAIL: grade B")

    if determine_letter_grade(75) == "C":
        print("PASS: grade C")
    else:
        print("FAIL: grade C")

    if determine_letter_grade(65) == "D":
        print("PASS: grade D")
    else:
        print("FAIL: grade D")

    if determine_letter_grade(50) == "F":
        print("PASS: grade F")
    else:
        print("FAIL: grade F")

    # Test determine_standing
    if determine_standing(95) == "Dean's List":
        print("PASS: Dean's List")
    else:
        print("FAIL: Dean's List")

    if determine_standing(80) == "Good Standing":
        print("PASS: Good Standing")
    else:
        print("FAIL: Good Standing")

    if determine_standing(65) == "Academic Probation":
        print("PASS: Academic Probation")
    else:
        print("FAIL: Academic Probation")

    if determine_standing(50) == "Academic Warning":
        print("PASS: Academic Warning")
    else:
        print("FAIL: Academic Warning")

    print("Tests finished.")


def main():
    """Run the Student Grade Tracker program."""
    name = get_student_name()
    scores = get_exam_scores(3)

    average = calculate_average(scores)
    grade = determine_letter_grade(average)
    standing = determine_standing(average)

    display_report(name, scores, average, grade, standing)


# Run tests first
test_grade_tracker()

print()

# Run main program
main()