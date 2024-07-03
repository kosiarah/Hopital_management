class User:
    def __init__(self, name, email, address, phone_number):
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return (f"Name: {self.name}, Email: {self.email}, Address: {self.address}, Phone no.: {self.phone_number}")  

class Account:
    def __init__(self, user, account_no, bank_name, account_balance = 0):
        self.user = user
        self.account_no = account_no
        self.bank_name = bank_name
        self.account_balance = account_balance

    def __str__(self):
        return (f"Account(User: {self.user}, Account Number: {self.account_no}, "
                f"Bank: {self.bank_name}, Balance: {self.account_balance})")


    def withdraw(self, amount):
         
         amount = int(input("Enter amount you would like to withdraw: "))
         while amount > self.account_balance:
             print("Insufficient balance")
             amount = int(input("Please enter a valid withdrawal amount: "))
             self.account_balance = self.account_balance - amount
             print("Withdrawal successful")


    def deposit(self, amount):
        if amount < 100:
            print("Can only deposit 100 and above")
        else:
            self.account_balance = self.account_balance + amount
            print("Deposit successful") 

    def check_balance(self):
        print(f"Your account balance is: ", self.account_balance)









user1 = User("kosi", "ksoss", "asasasa", "sddsdssds")
account = Account(user1, "2121212", "zenith", 1000)
print(account.account_balance)
account.withdraw(0)
print(account.account_balance)