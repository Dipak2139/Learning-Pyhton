attemps = 0
correct_pass = "abc1234"
chances = 3

while attemps<3:
    password= input("Enter the password: \n")
    if password == correct_pass:
        print("Access Granted...")
        break
    else:
        chances-=1
        print(f"You have {chances}  chances left ")
        attemps+=1


if attemps==3:
    print("You have Entered too many wrong password.. Please try after some time")