class Sample:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, a):
        self.a = a


s = Sample(1)
print(s.a)
