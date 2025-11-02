"""
1 - Create a BankAccount class with _balance, and methods deposit() and withdraw().
2 - Add a get_balance() method but don’t allow external code to change _balance directly.
3 - Add a rule: you can’t withdraw if the balance would go below 0.
"""
class BackAccount():
    def __init__(self) -> None:
        self._balance = float(0)

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount : float) -> None:
        self._balance += amount 

    def withdraw(self, amount) -> float:
        if self._balance < amount:
            print("You don't have enough money in your Bank Account")
            return
        self._balance -= amount
        return amount 


def main():
    bank_account = BackAccount()
    bank_account.deposit(2000)
    print(bank_account.get_balance())
    print(bank_account.withdraw(4000))
    print(bank_account.withdraw(400))
    print(bank_account.get_balance())
    
if __name__ == "__main__":
    main()
