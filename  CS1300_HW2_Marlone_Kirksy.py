word = input("Enter a word or phrase: ")

cleaned = word.lower().replace(" ", "")

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")