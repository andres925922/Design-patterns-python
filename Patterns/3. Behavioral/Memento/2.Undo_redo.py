class Memento:

    def __init__(self, balance) -> None:
        self.balance = balance

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.states = [Memento(self.balance)]
        self.points_in_time = 0

    def deposit(self, amount):
        self.balance += amount
        m = Memento(self.balance)
        self.states.append(m)
        self.points_in_time += 1
        return m
    
    def restore(self, memento: Memento):
        if memento:
            self.balance = memento.balance
            self.states.append(memento)
            self.points_in_time = len(self.states) - 1

    def undo(self):
        if self.points_in_time > 0:
            self.points_in_time -= 1
            m = self.states[self.points_in_time]
            self.balance = m.balance
            return m
        return None
        
    def redo(self):
        if self.points_in_time + 1 < len(self.states):
            self.points_in_time += 1
            m = self.states[self.points_in_time]
            self.balance = m.balance
            return m
        return None


    def __str__(self) -> str:
        return f'{self.balance}'

if __name__ == '__main__':
    ba = BankAccount(100)
    ba.deposit(100)
    ba.deposit(20)
    print(ba)

    ba.undo()
    ba.undo()
    print(ba)

    ba.redo()
    print(ba)