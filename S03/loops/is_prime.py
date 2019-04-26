number = 1
while number < 100:
    number += 1
    is_prime = True
    i = 1
    while i < (number - 1):
        i = i + 1
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(number)
