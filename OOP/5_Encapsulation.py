class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self._balance = balance  # Protected attribute

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposit of ${amount} successful. New balance: ${self._balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self._balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

# Creating an instance of the BankAccount class
account = BankAccount("123456789", 1000)

# Accessing account information using methods
print("Account Number:", account.get_account_number())  # Output: 123456789
print("Current Balance:", account.get_balance())  # Output: 1000

# Attempting to directly access protected attributes (which is discouraged but still possible)
print("Account Number (direct access):", account._account_number)  # Output: 123456789
print("Current Balance (direct access):", account._balance)  # Output: 1000

# Performing transactions
print(account.deposit(500))  # Output: Deposit of $500 successful. New balance: $1500
print(account.withdraw(200))  # Output: Withdrawal of $200 successful. New balance: $1300
