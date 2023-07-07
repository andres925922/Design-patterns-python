class Memento:

    def __init__(self, balance) -> None:
        self.balance = balance

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)
    
    def restore(self, memento: Memento):
        self.balance = memento.balance

    def __str__(self) -> str:
        return f'{self.balance}'

if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(100)
    m2 = ba.deposit(20)
    print(ba)

    ba.restore(m1)
    print(ba)