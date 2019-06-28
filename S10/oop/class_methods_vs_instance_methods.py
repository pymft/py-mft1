class Sample:
    instances = {}

    def __init__(self, name):
        self.name = name
        self.instances[name] = self

    @classmethod
    def count(cls):
        return len(cls.instances)

    def say_name(self):
        return self.name


a1 = Sample(1)
a2 = Sample(10)
a3 = Sample(16)
a4 = Sample(13)
a5 = Sample(14)



print(a1.say_name())
print(Sample.say_name(a1))
