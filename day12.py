# print("--- Age Verifier ---")

# try:
#     user_age = int(input("Please enter your age in numbers:\n"))
#     print("You are",user_age,"years old")
# except ValueError:
#     print("Error: YOu did not type a valid number.Go Again..!!")


print("---Uncrashable Calculator---")

is_running = True

while is_running:
    try:
        user = int(input("ENter a number to double:\n "))
        print("The doubled number is: \n",user*2)
        is_running = False
    except ValueError:
        print("Invalid..!! Please enter number only")

