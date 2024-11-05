#Write a Python program that accepts a sentence from the user and returns the sentence with
#each word reversed, but the order of words unchanged. For example, &quot;Hello World&quot; should become
#&quot;olleH dlroW&quot;.

user_input = input("Enter the String: ")
words = user_input.split()
print("Before reverse the words are: ",words)
result= " "

for word in words:
    ans = word[::-1]
    result+=ans+" "


print("After reverse the words are: ", result.split())
