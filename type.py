# To know the datatype of any any value we use type() function.

a = 56
b = type(a)
print(b) # <class 'int'>

c = "dipak"
print(type(c)) #<class 'str'>

# to change the type of any datatype we do the following things:

name = "33.5"
f = float(name)  # Conversion from String to float
print(type(f))

deepu = 123
g = str(deepu)
print(type(g)) # Conversion from Integer to String

ram = 23.555
h = int(ram)
print(type(h))  # Conversion from Floating point  to Integer