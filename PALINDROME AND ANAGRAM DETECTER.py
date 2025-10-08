# Palindrome check
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Anagram check
str1 = input("Enter first word: ")
str2 = input("Enter second word: ")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")