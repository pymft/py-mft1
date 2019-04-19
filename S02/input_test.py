value = input("please enter a number : ")

if not value.isdigit():
    print("cannot convert to numbers ")
else:

    num = int(value)
    if num % 3 == 0:
        print("3k ")
    elif num % 3 == 1:
        print("3k+1")
    else:
        print("3k + 2")

