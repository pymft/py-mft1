class MeaninglessTuple(tuple):
    def __getattribute__(self, item):
        if item[0] == '_' and item[1:].isdigit():
            indx = int(item[1:])
            return self[indx]
        return super().__getattribute__(item)


tup = MeaninglessTuple((1, 2, 3, 4))
tup.__getattribute__("whatever")
