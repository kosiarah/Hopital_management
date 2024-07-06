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


    def withdraw(self):
         
         
         while True:
             amount = int(input("Enter amount you would like to withdraw: "))
             if amount > self.account_balance:
                print("Insufficient balance")
             else:   
                self.account_balance = self.account_balance - amount
                print("Withdrawal successful")
                break


    def deposit(self):

        while True:
            amount = int(input("Enter amount you would like to deposit: "))
            if amount < 100:
                print("Can only deposit 100 and above")
            else:
                self.account_balance = self.account_balance + amount
                print("Deposit successful") 
                break

    def check_balance(self):
        print(f"Your account balance is: ", self.account_balance)



class Bank:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts  
    def get_account_names_and_details(self):
        for account_no, account in self.accounts.items():
            print(f"Account Number: {account_no}, Details: {account}")
        



"""
user1 = User("kosi", "ksoss", "asasasa", "sddsdssds")
account = Account(user1, "2121212", "zenith", 1000)
account.check_balance()
account.deposit()
account.check_balance()
"""

user1 = User("Kosi", "kosi@example.com", "123 Main St", "555-1234")
user2 = User("Arah", "arah@example.com", "456 Elm St", "555-5678")

account1 = Account(user1, "1001", "Bank A", 500)
account2 = Account(user2, "1002", "Bank A", 1500)

accounts_dict = {
    account1.account_no: account1,
    account2.account_no: account2
}
bank = Bank("Bank A", accounts_dict)

bank.get_account_names_and_details()
