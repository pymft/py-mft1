def multiplier_creator(const):
    def inner(n):
        answer = n * const
        return answer
    return inner


multiply_2 = multiplier_creator(2)
zarb_dar_se = multiplier_creator(3)
multiply_4 = multiplier_creator(4)
multiply_5 = multiplier_creator(5)
multiply_6 = multiplier_creator(6)
multiply_7 = multiplier_creator(7)

print(multiply_2(2), zarb_dar_se(2))