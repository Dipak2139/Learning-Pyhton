#Implement a function that checks whether a given string is a palindrome (a word, phrase, or sequence that reads the same backward as forward).

def palindrome_check(s):
    reverse = s[::-1]

    if (s==reverse):
        print("The string "+s+ " is a Palindrome String")
    else:
        print("The string "+s+ " is not a Palindrom String") 

user_input = input("Enter the String: ")
palindrome_check(user_input)
