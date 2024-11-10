def is_prime(num):

    if num ==1:
        return False
    elif num ==2:
        return True
    elif num%2==0:
        return False
    else:
        return True

num = int(input("Enter the number: "))
result = is_prime(num)
if(result==True):
    print(f"The number {num} is a prime number")
else:
    print(f"The number {num} is not a prime number")


print(is_prime(num))