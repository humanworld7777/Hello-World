class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner 
    self.__balance = balance
    
  def get_balance(self):
    return f"Balance: ${self.__balance}"

  def deposit(self, amount):
  if amount > 0:
    self>__balance += amount

acc = BankAccount("Yashwanth", 10000)
print(acc.get_balance())
