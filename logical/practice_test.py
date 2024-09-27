# Build python class for the models a simplified Banking system


class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return print("Insufficient funds")
        else:
            self.balance -= amount
        return print("Withdrawal successful")

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, target_account):
        if amount > self.balance:
            return print("Insufficient funds")
        else:
            self.balance -= amount
            target_account.deposit(amount)
        return print("Transfer successful")


if __name__ == "__main__":

    account1 = BankAccount("Alice", 500)
    account2 = BankAccount("Bob", 300)

    account1.deposit(200)
    print(account1.get_balance())  # Expected Output: 700

    account1.withdraw(1000)  # Expected Output: "Insufficient funds"
    print(account1.get_balance())  # Expected Output: 700

    account1.transfer(300, account2)
    print(account1.get_balance())  # Expected Output: 400
    print(account2.get_balance())  # Expected Output: 600
