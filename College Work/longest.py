# finding the longes word

def longest_word(s):
    word = s.split()
    return max(word, key=len)

sentence = "I love you Priya."
print(longest_word(sentence))