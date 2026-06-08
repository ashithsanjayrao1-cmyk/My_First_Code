###oops###

# class Phone:
#     def make_call(self):
#         print("Ringing ....Hellloo?")

# class Smartphone(Phone):
#     def browse_internet(self):
#         print("Opening Google chrome...")


# my_iphone = Smartphone()

# my_iphone.browse_internet()

# my_iphone.make_call()

###inheritance#####
# class BankAccount:
#     def __init__(self,account_holder,starting_balance):
#         self.owner= account_holder
#         self.balance= starting_balance
    
#     def deposit(self,amount):
#         self.balance = self.balance + amount
#         print("deposited amount",amount,"New balance is ",self.balance)

# class SavingsAccount(BankAccount):
#     def add_interest(self):
#         interest = self.balance * 0.05
#         self.balance = self.balance + interest
#         print("Interset added..!! New balance is",self.balance)


# #my_account = BankAccount("Ashith", 10000)
# #my_account.deposit(500)

# my_savings = SavingsAccount("Ashith", 1000)
# my_savings.deposit(500)

# my_savings.add_interest()


###polymorphism###

class Email:
    def send(self,message):
        print("Sending EMail:",message)


class SMS:
    def send(self,message):
        print("Sending TExt message",message)

alerts = [Email(),SMS()]

for method in alerts:
    method.send("You are hired")