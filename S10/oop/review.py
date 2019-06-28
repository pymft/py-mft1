class Sample:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return self.name



# s = object.__new__(Sample)
# s.__init__("Jack")
s = Sample("Jack")
a = Sample("John")
print(s.say_name())
print(a.say_name())


B = Sample
x = object.__new__(B)
x.__init__("someone")
B("someone")