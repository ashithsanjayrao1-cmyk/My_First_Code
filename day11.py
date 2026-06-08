# is_running = True

# while is_running:
#     print("\n----Main Menu---")
#     user_choice = input("Type 'stop' to exit, or anything else to continue:")

#     if user_choice == "stop":
#         print("Shutting down the machine.GoodByeeee!!!")
#         is_running = False
#     else:
#         print("YOu typed:",user_choice)
#         print("The loop is restarting....")

is_running = True

while is_running:
    print("\n---The Infinite ATM Menu---")
    print()
    user_choice = input("Type '1' to check balance, or Type '2' to withdraw cash....,or type '3' to stop ")
    if user_choice == '1':
        print("Your balance is $1000")
    elif user_choice == '2':
        print("WIthdrawing cash...!!")
    elif user_choice == '3':
        print("Good Byeee...!!!")
        is_running = False
    else:
        print("Give the correct input")
        
