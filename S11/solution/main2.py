import glob


class Node:
    _instances = {}

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self._instances[name] = self

    def set_parent(self, parent_number):
        obj = self._instances[parent_number]
        self.parent = obj
        obj.chidlren.appent(self)


list_of_files = glob.glob('./files/*.txt')
for f in list_of_files:
    child_name = f[8:-4]
    parent_name = open(f).read()
    n = Node(child_name)
    n.set_parent(parent_name)