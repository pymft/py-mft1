class Connector:
    FNAME = 'data'
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super().__new__(cls)
            cls._singleton.__initialized = False
        return cls._singleton

    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
            self.f = open(self.FNAME, 'w')

    def write_stuff(self, text):
        self.f.write(text)


c = Connector()
c.write_stuff("aaaaa")
c.write_stuff("bbb")
d = Connector()
d.write_stuff("ccccccccc")
c.write_stuff("dddddd")
print(c is d)
