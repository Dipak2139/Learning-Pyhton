#Write a function that removes all duplicate characters from a given string, keeping only the first
#occurrence of each character.


def remove_duplicates(s):

    result = " "
    for char in s:
        if char not in result:
            result+=char
    
    return result

user_input = input("Enter the String: ")
ans = remove_duplicates(user_input)
print(ans)


        