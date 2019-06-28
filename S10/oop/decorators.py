class ColorClass:
    mapping = {"red": 1, "green": 2, "yellow": 3, "blue": 4, "purple": 5}

    def __init__(self, color):
        self.__color = self.mapping[color]

    def __call__(self, f):
        def inner(*args, **kwargs):
            res = f"\033[3{self.__color};1m{f(*args, **kwargs)}\033[0m"
            return res

        return inner

def color(c):
    mapping = {"red": 1, "green": 2, "yellow": 3, "blue": 4, "purplr": 5}

    def decorator(f):
        def inner(*args, **kwargs):
            res = f"\033[3{mapping[c]};1m{f(*args, **kwargs)}\033[0m"
            return res

        return inner

    return decorator


@ColorClass("red")
def echo(s):
    return s


print(echo("Hello"))
