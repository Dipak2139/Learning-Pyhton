def sum_of_digits(num):

    convert = str(num)
    result = 0

    for i in convert:
        result+=int(i)
    
    return result


number=int(input("Enter a number: "))
a=sum_of_digits(number)
print(f"The sum of digits of the {number}  = ",a)
