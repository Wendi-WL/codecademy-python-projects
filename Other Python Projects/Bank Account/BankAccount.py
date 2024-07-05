class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "This account belongs to %s. The balance is: %.2f" % (self.name, self.balance)
  def show_balance(self):
    print("Balance: %.2f" % (self.balance))
  def deposit(self, amount):
    if amount <= 0:
      print("Error. Selected amount needs to be at least $0.01.")
      return
    else:
      print("Depositing %.2f to your account." % (amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount > self.balance:
      "Error. Account balance is less than desired withdrawal amount."
      return
    else:
      print("Withdrawing %.2f from your account." % (amount))
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Wendi")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)