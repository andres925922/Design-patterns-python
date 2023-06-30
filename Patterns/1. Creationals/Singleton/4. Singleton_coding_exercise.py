def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    a = factory()
    b = factory()
    # Now we check whether a is b
    response = a is b #True or false
    return response