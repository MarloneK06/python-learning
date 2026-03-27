# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Initialize counters
total_chars = len(sentence)
uppercase_count = 0
lowercase_count = 0
digit_count = 0
space_count = 0

# Loop through each character
for char in sentence:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    
    if char == " ":
        space_count += 1

# Reverse the sentence
reversed_sentence = sentence[::-1]

# Print the analysis
print("Total characters (including spaces):", total_chars)
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Digits:", digit_count)
print("Spaces:", space_count)
print("Reversed sentence:", reversed_sentence)