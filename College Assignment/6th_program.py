#Write a program that calculates and prints the frequency of each character in a given string. For
#example, for the string &quot;hello&quot;, the output should be: `{‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}`.

def calculate_char(input_string):
    
    frequency = {}

    for char in input_string:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    
    return frequency

user_input = input("Enter the String: ")
result = calculate_char(user_input)

print(result)