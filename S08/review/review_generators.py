def simple_generator():
    yield 10
    yield 20
    yield 3
    yield 15
    yield 1000
    yield 60
    yield 1


def fib():
    yield 1
    yield 1
    a, b = 1, 1
    while True:
        a, b = b, a+b
        yield b


for i in fib():
    print(i)
