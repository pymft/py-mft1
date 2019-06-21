class Hist:
    instances = []

    def __init__(self, name):
        self.name = name
        self.instances.append(self)



a = Hist("jack")
a = Hist("john")
a = Hist("emma")
print(id(a))