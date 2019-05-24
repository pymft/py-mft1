import math


def add_tags(tag):
    def inner_decorator(f):
        def inner(s):
            out = tag + str(f(s)) + tag
            return out

        return inner

    return inner_decorator


@add_tags("*")
@add_tags("&")
@add_tags("$")
def echo(s):
    return s


res = echo("hello")
print(res)
