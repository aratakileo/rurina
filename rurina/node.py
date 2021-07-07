import nodes_core


class Node:
    def __init__(self, x=0, y=0, name: str = ...):
        if name is ...:
            self.name = self.__class__.__name__
        self.nodes = []

        self.x, self.y = x, y

        nodes_core.get_nodes().append(self)

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, value):
        self.x, self.y = value

    def input(self, event):
        for node in self.nodes:
            node.input(event)


__all__ = ['Node', 'nodes_core']
