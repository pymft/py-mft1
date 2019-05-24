def fib():
    yield 1
    yield 1
    a, b = 1, 1
    while True:
        a, b = b, a + b
        yield b


storage = 0
for i, a in enumerate(fib()):
    storage += a.__sizeof__()
    print("{:10}, {}kB".format(i, storage / 1024))
