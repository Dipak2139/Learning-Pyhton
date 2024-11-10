def are_anagrams(s1,s2):

    str1 = s1.replace(" ","").lower()
    str2 = s2.replace(" ","").lower()

    return sorted(str1) == sorted(str2)

result = are_anagrams("Silent","Listen")
print(result)
