# 1. Check Palindrome

word = input("Enter a word to check palindrome: ")

if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# 2. Count Frequency of Each Character

text = input("Enter a string to count character frequency: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:")
for char, count in frequency.items():
    print(char, ":", count)


# 3. Reverse a Word

word = input("\nEnter a word to reverse: ")

print("Reversed word:", word[::-1])


# 4. Check Whether Two Strings Are Anagrams

str1 = input("\nEnter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


# 5. Find a Substring

string = input("\nEnter the main string: ")
substring = input("Enter the substring to find: ")

if substring in string:
    print("Substring found")
else:
    print("Substring not found")