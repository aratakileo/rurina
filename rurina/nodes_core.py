nodes = []


def get_nodes():
    global nodes
    return nodes


def input(event):
    for node in nodes:
        node.input(event)
