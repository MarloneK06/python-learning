# =========================
# UNIT 1: TUPLES EXERCISES
# =========================

# Beginner Exercise
rgb_color = (255, 128, 0)

print("Red:", rgb_color[0])
print("Green:", rgb_color[1])
print("Blue:", rgb_color[2])

palette = []
palette.append(rgb_color)
print("Palette:", palette)


# Intermediate Exercise
student1 = ("Alice", 90, 18)
student2 = ("Bob", 85, 19)
student3 = ("Charlie", 88, 18)

classroom = [student1, student2, student3]

# second student name
print("Second student name:", classroom[1][0])

# unpack first student
name, grade, age = classroom[0]
print("First student:", name, grade, age)


# Advanced Exercise
student = ("Alice", [80, 85, 90], 0)

# add fourth exam
student[1].append(95)

# calculate average
avg = sum(student[1]) / len(student[1])

# create new tuple (since tuples can't change)
updated_student = (student[0], student[1], avg)

print("Original:", student)
print("Updated:", updated_student)


# =========================
# UNIT 2: LIST VS TUPLE
# =========================

# Beginner Exercise
grades = [85, 90, 78]
today = (5, 6, 2026)

def boost_grades(grades):
    for i in range(len(grades)):
        grades[i] += 5

boost_grades(grades)
print("Boosted grades:", grades)

# comment:
# we use list for grades because it changes
# we use tuple for date because it should not change


# Intermediate Exercise
def find_range(*nums):
    return (min(nums), max(nums))

print(find_range(1, 5, 3))
print(find_range(2, 4, 6, 8, 10, 1, 7))

test_scores = [78, 92, 85, 88, 91]
print(find_range(*test_scores))


# Advanced Exercise
def calculate_statistics(*nums):
    count = len(nums)
    total = sum(nums)
    avg = total / count
    return (count, total, avg)

def update_student_records(records, bonus):
    new_list = []
    for name, grade in records:
        new_list.append((name, grade + bonus))
    return new_list

records = [("Alice", 85), ("Bob", 90)]
updated = update_student_records(records, 5)

print("Stats:", calculate_statistics(10, 20, 30))
print("Updated records:", updated)


# =========================
# UNIT 3: NESTED LISTS
# =========================

# Beginner Exercise
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Grid:", grid)
print("Center:", grid[1][1])

for row in grid:
    for val in row:
        print(val, end=" ")
    print()


# Intermediate Exercise
scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

passing_grades = [x for x in scores if x >= 60]

letter_grades = []
for g in passing_grades:
    if g >= 90:
        letter_grades.append("A")
    elif g >= 80:
        letter_grades.append("B")
    elif g >= 70:
        letter_grades.append("C")
    else:
        letter_grades.append("D")

print("Passing:", passing_grades)
print("Letters:", letter_grades)


# Advanced Exercise
table = [[i * j for j in range(1, 5)] for i in range(1, 5)]

print("Multiplication Table:")
for row in table:
    print(row)

def sum_diagonal(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

print("Diagonal sum:", sum_diagonal(table))

# generator for even numbers
gen = (x for row in table for x in row if x % 2 == 0)

print("First 5 even numbers:")
count = 0
for num in gen:
    print(num)
    count += 1
    if count == 5:
        break