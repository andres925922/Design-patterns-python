# Copyright (c) 2023 Andres Convertini
#
# -*- coding:utf-8 -*-
# @Script: 1-Functional_decorators.py
# @Author: Andres Convertini
# @Email: andres.convertini91@gmail.com
# @Create At: 2023-07-06 06:37:16
# @Last Modified By: Andres Convertini
# @Last Modified At: 2023-07-06 06:37:16
# @Description: This is description.



import time

def time_it(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Execution duration {int(end - start) * 1000} ms')
        return
    return wrapper


@time_it
def my_function():

    time.sleep(3)
    return

if __name__ == "__main__":

    my_function()

    # time_it(my_function)()