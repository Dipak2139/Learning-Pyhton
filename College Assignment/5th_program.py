#Implement a function that checks whether a given string is a palindrome (a word, phrase, or sequence that reads the same backward as forward).

user_input = input("Enter the String: ")
reverse = user_input[::-1]

if (user_input==reverse):
    print("The string "+user_input+ " is a Palindrome String")
else:
    print("The string "+user_input+ " is not a Palindrom String") 