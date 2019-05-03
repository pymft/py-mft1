left = lambda lst: lst[:len(lst) // 2] + lst[:len(lst) // 2][::-1]
right = lambda lst: lst[len(lst) // 2:][::-1] + lst[len(lst) // 2:]


def new_left(lst):
    """
    return the left mirror of a list

    :param lst: list
    :return:
    """
    mid = len(lst) // 2
    left_side_of_list = lst[:mid]
    mirror = left_side_of_list[::-1]
    concat_lst = left_side_of_list + mirror
    return concat_lst


inp = list(range(1, 41))
print(left(inp))
print(new_left(inp))

