import time


# pass function into a function
def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def decoratot(function, x, y):
    return function(x, y)


print(decoratot(add, 2, 3))

print(decoratot(multiply, 3, 4))


# decorator function
def delay_decorator(function):
    def wrapper_function():
        time.sleep(1)
        # Do something before
        function()
        time.sleep(1)
        function()
        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


say_hello()
