def generator_range(stop):
    i = 0
    while i < stop:
        i += 1
        yield i



numbers = generator_range(100)
print(next(numbers))
print(next(numbers))