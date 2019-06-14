range(10)
range(5, 10)
range(2, 10, 2)


inputs = (5, 10)
range(*inputs)


def new_sum(*args, **kwargs):
    print(kwargs)
    print(args)




new_sum(1, 2, 3, z=1 , mode="dsgjdlkg", aaa=1234)



