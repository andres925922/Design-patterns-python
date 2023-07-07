"""
Command Coding Exercise
Implement the Account.process()  method to process different account commands.

The rules are obvious:

success indicates whether the operation was successful

You can only withdraw money if you have enough in your account
"""
from enum import Enum

class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False

class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return True

    def withdraw(self, amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        return True

    def process(self, command: Command):
        # todo
        if command.action == Command.Action.DEPOSIT:
            command.success = self.deposit(command.amount)
        elif command.action == Command.Action.WITHDRAW:
            command.success = self.withdraw(command.amount)
        else:
            command.success = False




    # a = Account()

    # cmd = Command(Command.Action.DEPOSIT, 100)
    # a.deposit(100)
    # a.process(cmd)
    # print(a.balance, cmd.action == Command.Action.DEPOSIT)
