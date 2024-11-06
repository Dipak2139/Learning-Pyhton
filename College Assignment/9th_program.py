#Write a function that accepts a sentence as input and returns the longest word in the sentence. If
#there are multiple words of the same length, return the first one.

def longest_word(sentence):
    
    words = sentence.split()
    longest = " "

    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

input_string = input("Enter a Sentence: ")
result = longest_word(input_string)
print("The longest word is: ",result)