"""

"""

# Copyright (c) 2023 Andres Convertini
#
# -*- coding:utf-8 -*-
# @Script: Event.py
# @Author: Andres Convertini
# @Email: andres.convertini91@gmail.com
# @Create At: 2023-07-10 04:19:59
# @Last Modified By: Andres Convertini
# @Last Modified At: 2023-07-10 04:34:14
# @Description: This is description.

class Event(list):
    # List of functions that need to be invoked whenever this event actually happens
    def __call__(self, *arg, **kwargs):
        for item in self:
            item(*arg, **kwargs)

class Person:

    def __init__(self, name, address):
        self.address = address
        self.name = name
        self.falls_ill = Event()            # List of functions -> events -> it is callable
    
    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'{name} needs a doctor in {address}')

if __name__ == '__main__':
    person = Person('Sherlok', '221b Baker st')
    person.falls_ill.append(call_doctor)
    person.falls_ill.append(
        lambda name, address: print(f'{name} is ill and needs a doctor in {address}')
    )
    person.catch_a_cold()

    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()