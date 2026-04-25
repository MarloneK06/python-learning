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

uppercase_version = sentence.upper()
lowercase_version = sentence.lower()
reversed_sentence = sentence[::-1]

starts_with_capital = sentence[0].isupper()
ends_with_punctuation = sentence.endswith((".", "!", "?"))

print("--- Analysis Results ---")
print(f"Total characters (with spaces): {total_with_spaces}")
print(f"Total characters (without spaces): {total_without_spaces}")
print(f"Number of words: {word_count}")
print(f"Number of vowels: {vowel_count}")
print(f"Uppercase version: {uppercase_version}")
print(f"Lowercase version: {lowercase_version}")
print(f"Reversed: {reversed_sentence}")

if starts_with_capital:
    print("Starts with capital: Yes")
else:
    print("Starts with capital: No")

if ends_with_punctuation:
    print("Ends with punctuation: Yes")
else:
    print("Ends with punctuation: No")