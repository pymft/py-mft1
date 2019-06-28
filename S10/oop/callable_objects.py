class Sample:
    def __init__(self, name):
        self.name = name


    def __call__(self):
        return self.name


s1 = Sample("Hello")
print(s1())