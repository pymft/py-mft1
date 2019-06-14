def say_hello():
    return "hello"


def say_goodbye():
    return "goodbye"


def say_something():
    return "something"


def say(word):
    def say_word():
        return word
    return say_word


def decorator(f):
    def inner(*args):
        out = f(*args)
        res = "*" + str(out) + "*"
        return res
    return inner


@decorator
@decorator
def fun(a, b, c):
    return a, c, b


print(fun(1, 2, 3))