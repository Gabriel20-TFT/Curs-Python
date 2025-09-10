class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}.")
            return True
        else:
            print("Deposit amount must be positive.")
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}.")
            return True
        else:
            print("Withdraw amount must be between 0 and balance.")
            return False

    def __str__(self):
        return f"Bank Account (Owner: {self.owner}, Balance: {self.balance})"

if __name__ == "__main__":
    persoana_1 = Person("Catalin", "Breaz", 26)

    bankAccount = BankAccount(owner=persoana_1)

    print(bankAccount)
    bankAccount.deposit(100)
    print(bankAccount)
    bankAccount.withdraw(500)
    print(bankAccount)