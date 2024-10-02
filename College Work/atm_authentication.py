#Step 1 
user_password ="abcd1234"
attempts = 0
withdrawls = 0

while attempts<3:
    check_pass = input("Enter the password: ")
    if user_password == check_pass:
        print("Access Granted...")
        while withdrawls<3:
            amount = int(input("Enter the withdrawl amount: \n"))
            print(f"Withdrawl amount: {amount}")
            withdrawls+=1
            print(f"Withdrawls left {3-withdrawls}")
            if withdrawls==3:
                print("you have reached the maximum withdrawl limit")
        break
    else:
        attempts+=1
        print(f"You have {3-attempts} attempts left")

if attempts==3:
    print("Your card has been blocked...")
    exit()


