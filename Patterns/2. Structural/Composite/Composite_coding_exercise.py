
"""

Composite Coding Exercise
Consider the code presented below. We have two classes called SingleValue and ManyValues. SingleValue stores just one numeric value, but ManyValues can store either numeric values or SingleValue objects.

You are asked to give both SingleValue and ManyValues a property member called sum that returns a sum of all the values that the object contains. Please ensure that there is only a single method that realizes the property sum, not multiple methods.

"""
from abc import ABC
from collections.abc import Iterable

class Value(list, ABC):

    @property
    def sum(self):
        result = []
        for c in self:
            for i in c:
                result.append(i)
        return sum(result)

class SingleValue(Value):
    def __init__(self, value):
        self.value = value

    # We convert this single value into an iterable
    def __iter__(self):
        yield self.value

class ManyValues( Value):
    pass

