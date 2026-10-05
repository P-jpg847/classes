# A class is defined with the keyword 'class' followed by the class name and a colon. The body of the class is indented and contains methods and attributes that define the behavior and state of the class.

class NameofClass:
    #class def go here
    pass 

class BankAccount:
    pass

peters_account = BankAccount()
peters_account.owner = "Peter Python"
peters_account.balance = 5.0

print(peters_account.owner)
print(peters_account.balance)

class BankAccount2:
    #constructors are useful because they let us create an object and set its initial state in one step, making it easier to work with consistent data every time a new instance is created.
    def _init_(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

#as the method is called, no argument should be given for the self parameter, as it is automatically passed by Python.

peters2_account = BankAccount2(5.0, "Peter Python")
paulas_account = BankAccount2(10.0, "Paula Python")

print(peters2_account.owner)
print(paulas_account.balance)