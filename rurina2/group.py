nodes_groups = []
groups = []


class Group:
    def __init__(self):
        self.__gindex__ = len(nodes_groups)
        nodes_groups.append([])

        groups.append(self)

    def __len__(self):
        return len(nodes_groups[self.__gindex__])

    def __del__(self):
        for node in nodes_groups[self.__gindex__]:
            self.remove(node)

        nodes_groups.remove(nodes_groups[self.__gindex__])
        groups.remove(self)

    @property
    def nodes(self) -> list:
        return nodes_groups[self.__gindex__]

    @property
    def next(self):
        if self.__gindex__ == len(groups) - 1:
            return groups[0]
        else:
            return groups[self.__gindex__ + 1]

    @property
    def prev(self):
        if self.__gindex__ == 0:
            return groups[len(groups) - 1]
        else:
            return groups[self.__gindex__ - 1]

    def append(self, node):
        for group in nodes_groups:
            if node in group:
                group.remove(node)
                break

        nodes_groups[self.__gindex__].append(node)

    def remove(self, node):
        nodes_groups[self.__gindex__].remove(node)
        nodes_groups[0].append(node)

    def clear(self):
        nodes_groups[self.__gindex__] = []


rootgroup = Group()


__all__ = [
    'Group',
    'rootgroup'
]
