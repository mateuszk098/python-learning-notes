"""
Simple class BankAccount with private attributes.
"""


class BankAccount:
    def __init__(self, account_holder):
        self._balance = 0
        self._name = account_holder
        with open(f"{self._name}_book.txt", "w", encoding="utf-8") as ledger_file:
            ledger_file.write("Account Balance is 0.\n")

    def deposit(self, amount):
        if amount <= 0:
            return  # Cannot make negative deposit.
        self._balance += amount
        with open(f"{self._name}_book.txt", "a", encoding="utf-8") as ledger_file:
            ledger_file.write(f"Deposit: {amount}\n")
            ledger_file.write(f"Account Balance is {self._balance}\n")

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return  # Not enough money or negative withdraw attempt.
        self._balance -= amount
        with open(f"{self._name}_book.txt", "a", encoding="utf-8") as ledger_file:
            ledger_file.write(f"Withdraw: {amount}\n")
            ledger_file.write(f"Account Balance is {self._balance}\n")


acct = BankAccount("Alicja")
acct.deposit(120)
acct.withdraw(40)

acct._balance = 1_000_000
acct.withdraw(1000)
acct._name = "Marta"
acct.withdraw(1000)
