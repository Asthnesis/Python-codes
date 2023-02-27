class BankAccount:
 def __init__(self,customer_name,account_number,balance,date_of_opening):
    self.account_number = account_number
    self.balance = balance
    self.date_of_opening = date_of_opening
    self.customer_name = customer_name
 def deposit(self):
   '''Return deposited amount'''
   deposit = int(input("Enter Deposit amount: "))
   self.balance = deposit + self.balance
   print("New balance: ",self.balance)
 def withdraw(self):
    '''return insuffient bal if amount to be withdrawn < balance else return amount that has been withdrawn'''
    withdrawal_amt = int(input("Enter amount to withdraw: "))
    if (withdrawal_amt > self.balance):
       print("Insufficient Balance")
    else:
       self.balance = self.balance - withdrawal_amt
       print("Amount to withdraw: ",withdrawal_amt)
 def check_balance(self):
    '''Print current balance'''
    print("Account Balance: ",self.balance)
 def customer_details(self):
    '''print customer name, a/c number, date of account opening and balance'''
    print(self.customer_name,self.account_number,self.date_of_opening)

Bank = BankAccount("Name: James Mwangi","A/c: 001",4000,"Account opened: 3rd September 2020")
Bank.deposit()
Bank.withdraw()
Bank.check_balance()
Bank.customer_details()