# CS1300 Homework 2
# Marlone Kirksy

# -----------------------------
# Problem 1: User Profile Generator
# -----------------------------

first = input("Enter first name: ").title()
last = input("Enter last name: ").title()
birth_year = int(input("Enter birth year: "))
hobby = input("Enter favorite hobby: ").title()

age = 2026 - birth_year

print("=" * 36)
print(" USER PROFILE CARD ")
print("=" * 36)
print(f"Name: {first} {last}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print("-" * 36)
print("Thank you for creating your profile!")
print("=" * 36)


# -----------------------------
# Problem 2: Text Analyzer
# -----------------------------

print("=== TEXT ANALYZER ===")

sentence = input("Enter a sentence: ")

total_with_spaces = len(sentence)
total_without_spaces = len(sentence.replace(" ", ""))
word_count = len(sentence.split())

vowels = "aeiou"
vowel_count = 0

for char in sentence.lower():
    if char in vowels:
        vowel_count += 1

print("--- Analysis Results ---")
print(f"Total characters (with spaces): {total_with_spaces}")
print(f"Total characters (without spaces): {total_without_spaces}")
print(f"Number of words: {word_count}")
print(f"Number of vowels: {vowel_count}")
print(f"Uppercase version: {sentence.upper()}")
print(f"Lowercase version: {sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")


# -----------------------------
# Bonus: Palindrome Checker
# -----------------------------

word = input("Enter a word or phrase: ")

cleaned = word.lower().replace(" ", "")

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")