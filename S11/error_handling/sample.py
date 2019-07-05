def div(a, b):
    res = a / b
    return res

lst = [1, 2, 3]

try:
    print(div(10, 0))
    print(lst[10])
    print(text)
except ZeroDivisionError:
    print("ZeroDivisionError")
except IndexError:
    print("IndexError")
except NameError as e:
    print("Name error", e.args)
