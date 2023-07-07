
import unittest

from Command_coding_exercise import *

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
