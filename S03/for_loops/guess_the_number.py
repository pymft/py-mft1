import random

upper_limit = 1024
secret = random.randint(1, upper_limit)
# print(secret)

for _ in range(11):
    guess = eval(input("guess the number : "))
    if guess > secret:
        print("your number is \033[34;1m greater \033[0m than the secret number")
    elif guess < secret:
        print("your number is \033[31;1m lesser \033[0m than the secret number")
    else:
        print("BINGO!!!")
        break


