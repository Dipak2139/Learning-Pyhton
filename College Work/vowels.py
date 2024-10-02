#vowels counter

def count_vowels(s):
    sum=0

    vowels="aeiouAEIOU"
    for char in s:
        if char in vowels:
            sum+=1
    return (sum)

sentence = "Dipak"
print(count_vowels(sentence))
