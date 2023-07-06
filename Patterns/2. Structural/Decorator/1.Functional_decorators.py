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