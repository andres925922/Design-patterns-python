"""
State Coding Exercise
A combination lock is a lock that opens after the right digits have been entered. A lock is preprogrammed with a combination (e.g., 12345 ) and the user is expected to enter this combination to unlock the lock.

The lock has a Status field that indicates the state of the lock. The rules are:

If the lock has just been locked (or at startup), the status is LOCKED.

If a digit has been entered, that digit is shown on the screen. As the user enters more digits, they are added to Status.

If the user has entered the correct sequence of digits, the lock status changes to OPEN.

If the user enters an incorrect sequence of digits, the lock status changes to ERROR.

Please implement the CombinationLock  class to enable this behavior. Be sure to test both correct and incorrect inputs.
"""

class CombinationLock:
    def __init__(self, combination: list):

        self.combination = combination
        self.reset()
        # todo

    def reset(self):
        self.status = 'LOCKED'
        self.inputs = []

    def enter_digit(self, digit):

        self.inputs.append(digit)
        self.status = ''.join([str(i) for i in self.inputs])

        if len(self.combination) == len(self.inputs):
            if self.combination == self.inputs:
                self.inputs = []
                self.status = 'OPEN'
                return
            else:
                self.reset()
                self.status = 'ERROR'


        

            
        