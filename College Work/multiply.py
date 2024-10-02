table = int(input("Enter the number you wish to see the multiplication table= \n"))

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i * j, end="\t")
#     print()

for i in range(1,11):
    mul = table * i
    print(f"{table} * {i} = {mul}")