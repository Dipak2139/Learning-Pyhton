#Write a Python program that accepts a string from the user and counts the number of vowels and
#consonants.

user_input = input("Enter a String: ")
vowels = 0
consonants = 0
for char in user_input:
    if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A'or  char=='E' or char=='I' or char=='O'or char =='U'):
        vowels=vowels+1
    elif char in user_input:
        consonants = consonants + 1

print("The total vowels count in the string " + user_input + " is: ",vowels) 
print("The total consonants count in the string " + user_input + " is: ",consonants) 
