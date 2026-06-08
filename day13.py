# class Student:

#     def __init__(self,student_name,student_score):
#         self.name = student_name
#         self.score = student_score

#     def display_profile(self):
#         print("Student:",self.name,"| Score:",self.score)

# student1 = Student("AShith",95)
# student2 = Student("Rahul", 75)

# student1.display_profile()
# student2.display_profile()

class BankAccount:
    def __init__(self,account_holder,starting_balance):
        self.owner= account_holder
        self.balance= starting_balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("deposited amount",amount,"New balance is ",self.balance)

my_account = BankAccount("Ashith", 10000)
my_account.deposit(500)