email = input("Enter an email: ")

at_count = 0
space_count = 0

# Count @ and spaces
for ch in email:
    if ch == "@":
        at_count += 1
    if ch == " ":
        space_count += 1

criteria = 0

# 1. Exactly one @
if at_count == 1:
    print("1. Pass")
    criteria += 1
else:
    print("1. Fail")

# Find @ index
at_index = -1
for i in range(len(email)):
    if email[i] == "@":
        at_index = i

# 2. At least one character before @
if at_index > 0:
    print("2. Pass")
    criteria += 1
else:
    print("2. Fail")

# 3. At least one dot after @
dot_found = False
for i in range(at_index + 1, len(email)):
    if email[i] == ".":
        dot_found = True

if dot_found:
    print("3. Pass")
    criteria += 1
else:
    print("3. Fail")

# 4. At least two characters after last dot
last_dot = -1
for i in range(len(email)):
    if email[i] == ".":
        last_dot = i

if last_dot != -1 and len(email) - last_dot - 1 >= 2:
    print("4. Pass")
    criteria += 1
else:
    print("4. Fail")

# 5. No spaces
if space_count == 0:
    print("5. Pass")
    criteria += 1
else:
    print("5. Fail")

# Final result
if criteria == 5:
    print("Valid email address")
elif criteria >= 3:
    print("Possibly valid - review format")
else:
    print("Invalid email address")