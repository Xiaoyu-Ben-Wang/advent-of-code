from timeit import default_timer as timer
from datetime import timedelta


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.connections = []

    def __repr__(self) -> str:
        connectionNames = [str(node.name) for node in self.connections]
        return f"{self.name}: [{', '.join(connectionNames)}]"


def partOne(f):
    nodes = dict()
    data = f.read().splitlines()
    for connection in data:
        name1, name2 = connection.split('-')
        node1 = nodes.get(name1, Node(name1))
        node2 = nodes.get(name2, Node(name2))
        node1.connections.append(node2)
        node2.connections.append(node1)
        nodes[name1] = node1
        nodes[name2] = node2

    disallowed = set()
    return DFS(nodes['start'], disallowed)


def DFS(currNode: Node, visited: set):
    disallowed = visited.copy()
    count = 0
    if currNode.name == 'end':
        return 1
    elif currNode.name in disallowed:
        return 0

    if currNode.name.islower():
        disallowed.add(currNode.name)

    for conn in currNode.connections:
        count += DFS(conn, disallowed)

    return count


def DFS2(currNode: Node, visited: set, vistedExtra: bool):
    disallowed = visited.copy()
    count = 0

    if currNode.name == 'end':
        return 1
    elif currNode.name in disallowed and currNode.name == 'start':
        return 0
    elif currNode.name in disallowed and vistedExtra:
        return 0
    elif currNode.name in disallowed:
        for conn in currNode.connections:
            count += DFS2(conn, disallowed, True)
        return count

    if currNode.name.islower():
        disallowed.add(currNode.name)

    for conn in currNode.connections:
        count += DFS2(conn, disallowed, vistedExtra=vistedExtra)
    return count


def partTwo(f):
    nodes = dict()
    data = f.read().splitlines()
    for connection in data:
        name1, name2 = connection.split('-')
        node1 = nodes.get(name1, Node(name1))
        node2 = nodes.get(name2, Node(name2))
        node1.connections.append(node2)
        node2.connections.append(node1)
        nodes[name1] = node1
        nodes[name2] = node2

    disallowed = set()
    return DFS2(nodes['start'], disallowed, False)


if __name__ == '__main__':
    with open('12.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
