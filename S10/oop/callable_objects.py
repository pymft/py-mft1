class Sample:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return self.name


insatnce1 = Sample("Hello")
insatnce2 = Sample("Hi")
res = insatnce1()
print(res)
res = insatnce2()
print(res)
