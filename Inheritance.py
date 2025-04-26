class Bank():
  def __init__(self,account_holder,account_number,balance):
    self.account_holder = account_holder
    self.account_number = account_number
    self.balance = balance
  def deposit(self):
    choose = input("Do you want to deposit anything?")
    if choose == "Yes":
      num = int(input("Enter how much you want to deposit"))
      self.balance = self.balance + num
      print("Sucessfully added")
  def withdraw(self):
    choose2 = input("Do you want to withdraw anything?")
    if choose2 == "Yes":
      num2 = int(input("Enter how much you want to withdraw"))
      if num2 > self.balance:
        print("Sorry, you do not have enough money")
      elif num2 <= self.balance:
        self.balance = self.balance - num2
        print("You have sucessfully withdrawn your money")
  def get_balance(self):
    choose3 = input("Do you want to get your balance")
    if choose3 == "Yes":
      print(self.balance)
  def display_account_info(self):
    choose4 = input("Do you want to display your account information")
    if choose4 == "Yes":
      print(self.account_holder,"", self.account_number, "",self.balance)

class Savings_account(Bank):
  def __init__(self, account_holder, account_number, balance, interest_rate):
    super().__init__(account_holder,account_number,balance)
    self.interest_rate = interest_rate
  def add_interest(self):
    interest = self.interest_rate/100
    addin = self.balance*interest
    self.balance = self.balance + addin
    print(self.balance)
# bank1 = Bank("Srihith", "52", 10000)
# bank1.deposit()
# bank1.withdraw()
# bank1.get_balance()
# bank1.display_account_info()
saving1 = Savings_account("Srihith", "52", 10000, 2)
saving1.deposit()
saving1.withdraw()
saving1.get_balance()
saving1.display_account_info()
saving1.add_interest()