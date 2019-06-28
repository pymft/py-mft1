class Sample:
    instances = {}

    def __init__(self, name):
        self.name = name
        self.instances[name] = self

    @classmethod
    def count(cls):
        return len(cls.instances)

