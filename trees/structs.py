class Node():

    def __init__(self, val, children, name=None):
        self._val = val
        self._children = children
        self._name = name

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = children

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Graph():

    def __init__(self, root):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root
