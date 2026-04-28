# CS1300_HW4_Marlone_Kirksy.py

# Movie Ticket Pricing
print("Problem 1")

age = int(input("Enter your age: "))
matinee_input = input("Is this a matinee showing? (yes/no): ")
matinee = True if matinee_input.lower() == "yes" else False

if age < 0:
    print("Error: Age cannot be negative")
else:
    if age < 13:
        group = "Child"
        if matinee:
            price = 6.00
        else:
            price = 8.00

    elif age <= 17:
        group = "Teen"
        if matinee:
            price = 7.00
        else:
            price = 10.00

    elif age <= 64:
        group = "Adult"
        if matinee:
            price = 8.00
        else:
            price = 13.00

    else:
        group = "Senior"
        if matinee:
            price = 6.00
        else:
            price = 7.00

    print("Age group:", group)
    print("Ticket price: $", format(price, ".2f"))


# Input Validator
print("\nProblem 2")

errors = []

student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")

# Student ID
if len(student_id) != 8:
    errors.append("Student ID must be exactly 8 characters")

if len(student_id) > 0:
    if not student_id[0].isalpha():
        errors.append("Student ID must start with a letter")

if len(student_id) == 8:
    if not student_id[1:].isdigit():
        errors.append("Last 7 characters must be digits")

# Name
if name.strip() == "":
    errors.append("Name cannot be empty")

# Age
try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except:
    errors.append("Age must be a valid integer")

# Major
if major.upper() not in ["CS", "IT", "CE", "DS"]:
    errors.append("Major must be CS, IT, CE, or DS")

# Output
if len(errors) == 0:
    print("Profile created successfully")
    print("Student ID:", student_id)
    print("Name:", name)
    print("Age:", age)
    print("Major:", major.upper())
else:
    print("Profile has errors:")
    for x in errors:
        print("-", x)


# Campus Cafe Menu
print("\nCAMPUS CAFE")
print("1. Coffee - $3.50")
print("2. Sandwich - $6.00")
print("3. Salad - $5.50")
print("4. Combo - $8.00")
print("5. Exit")

choice = input("Enter your choice (1-5): ")

item = ""
price = 0

if choice == "1":
    item = "Coffee"
    size = input("Enter size (small/medium/large): ").lower()

    if size == "medium":
        price = 4.50
        item = "Coffee Medium"
    elif size == "large":
        price = 5.50
        item = "Coffee Large"
    else:
        price = 3.50
        item = "Coffee Small"

elif choice == "2":
    item = "Sandwich"
    price = 6.00
    cheese = input("Add cheese? (yes/no): ").lower()

    if cheese == "yes":
        price = price + 0.75
        item = "Sandwich + Cheese"

elif choice == "3":
    item = "Salad"
    price = 5.50
    dressing = input("Enter dressing: ").lower()

    if dressing not in ["ranch", "italian", "vinaigrette", "none"]:
        dressing = "none"

    item = "Salad " + dressing

elif choice == "4":
    item = "Combo"
    price = 8.00

    size = input("Enter coffee size: ").lower()
    if size == "medium":
        price = price + 1
    elif size == "large":
        price = price + 2

    cheese = input("Add cheese? (yes/no): ").lower()
    if cheese == "yes":
        price = price + 0.75

elif choice == "5":
    print("Goodbye")

else:
    print("Invalid choice")

if choice == "1" or choice == "2" or choice == "3" or choice == "4":
    customer = input("Enter your name: ")

    try:
        quantity = int(input("How many? "))
        if quantity <= 0:
            quantity = 1
    except:
        quantity = 1

    subtotal = price * quantity
    tax = subtotal * 0.07
    total = subtotal + tax

    print("\nORDER RECEIPT")
    print("Customer:", customer)
    print("Item:", item)
    print("Quantity:", quantity)
    print("Unit Price: $", format(price, ".2f"))
    print("Subtotal: $", format(subtotal, ".2f"))
    print("Tax: $", format(tax, ".2f"))
    print("Total: $", format(total, ".2f"))
