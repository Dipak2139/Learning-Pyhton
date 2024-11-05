#Write a Python program that takes a sentence as input, splits it into words, and prints the words
#sorted alphabetically.

user_input = input("Enter a String: ")
words = user_input.split()
print(words)
sorted_words = sorted(words)
print(sorted_words)