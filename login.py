password = "1234"

chances = 3
attemps = 0
i=1

while(i<=chances):
    user = input("Enter your password??")
    if(password==user): 
        print("You have successfully login")
        break
    else:
        print(f"you have got more {3-i} chances.")
        attemps+=1 
    
    i=i+1

if(attemps==3):
    print('Please try after 1 day')