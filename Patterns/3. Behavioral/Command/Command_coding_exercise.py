"""
Command Coding Exercise
Implement the Account.process()  method to process different account commands.

The rules are obvious:

success indicates whether the operation was successful

You can only withdraw money if you have enough in your account
"""

import unittest

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



class Evaluate(unittest.TestCase):
    def test_1(self):
        a = Account()

        cmd = Command(Command.Action.DEPOSIT, 100)
        a.process(cmd)

        self.assertEqual(100, a.balance)
        self.assertTrue(cmd.success)

    def test_2(self):
        a = Account()

        cmd = Command(Command.Action.DEPOSIT, 100)
        a.process(cmd)

        cmd = Command(Command.Action.WITHDRAW, 50)
        a.process(cmd)
        print(a.balance)

        self.assertEqual(50, a.balance)
        self.assertTrue(cmd.success)


        cmd.amount = 150
        a.process(cmd)

        self.assertEqual(50, a.balance)
        self.assertFalse(cmd.success)

if __name__ == '__main__':
    unittest.main()

    # a = Account()

    # cmd = Command(Command.Action.DEPOSIT, 100)
    # a.deposit(100)
    # a.process(cmd)
    # print(a.balance, cmd.action == Command.Action.DEPOSIT)
