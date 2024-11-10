def is_amstrong(num):

    convert = str(num)
    total_digits = len(convert)
    total = 0

    for num in convert:
        total+= int(num)**total_digits
    
    return num==total

number = int(input("Enter the number: "))

if(is_amstrong(number)):
    print(f"{number} is a Amstrong number")
else:
    print(f"{number} is not a Amstrong number")
