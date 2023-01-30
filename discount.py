#discount of 5% if amount exceedes 1000
amount = int(input("Enter amount: "))
discount = 5/100
if amount >= 1000:
  discounted_amt = discount*amount
print("Discount = ",discounted_amt)