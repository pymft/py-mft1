class NonIntegerValueOfFactorial(ArithmeticError):
    pass

class NegativeValueOfFactorial(ArithmeticError):
    pass




def fact(n):
    if not isinstance(n, int):
        raise NonIntegerValueOfFactorial("invalid type ")

    if n < 0:
        raise NegativeValueOfFactorial
    out = 1

    while n > 0:
        out *= n
        n -= 1

    return out


try:
    print(fact(-19))
except NonIntegerValueOfFactorial as e:
    print(e)
except NegativeValueOfFactorial as e:
    print(e)
