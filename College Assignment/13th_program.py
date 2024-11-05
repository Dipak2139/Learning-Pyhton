#Write a program that extracts all the digits from a given string and prints them. For example, if
#the input is &quot;abc123xyz45&quot;, the output should be `12345`.

user_input = input("Enter the String: ")
print("Original String: ",user_input)
result=''

for char in user_input:
    if (char=='1' or char=='2' or char=='3' or char=='4' or char=='5' or char=='6' or char=='7' or char=='8' or char=='9'):
        result+=char

print("After extracting numbers from the given string: ", result)