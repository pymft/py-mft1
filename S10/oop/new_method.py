class Sample:
    instances = {}

    def __new__(cls, name):
        if name in cls.instances:
            return cls.instances[name]
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        self.instances[name] = self


a = Sample("A")
b = Sample("B")

print(id(a))
print(id(b))