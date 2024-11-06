#Create a Python program that replaces all occurrences of a given substring with another substring
#in a string. For example, in the string &quot;Hello World&quot;, replace &quot;World&quot; with &quot;Everyone&quot;.

input_string = "Hello World"
print("Original String: ",input_string)
result = input_string.replace("World", "Everyone")
print("After replacing the string "+input_string+" we get: ",result)
