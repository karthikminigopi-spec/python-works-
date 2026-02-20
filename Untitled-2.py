class BankAccount:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display_balance(self):
        print("\nAccount Holder:", self.holder_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Create object
acc = BankAccount("KARTHIK", "890675", 5000)

# Call methods
acc.display_balance()
acc.deposit(1000)
acc.withdraw(2000)
acc.display_balance()