import re
from datetime import timedelta
from io import TextIOWrapper
from timeit import default_timer as timer


class Monkey:
    def __init__(self, operation, dependents=None) -> None:
        self.dependents = dependents
        self.operation = operation

    def __repr__(self) -> str:
        return f'(operation: {self.operation}, dependents: {self.dependents})'


def partOne(f: TextIOWrapper):
    PATTERN = r' ?(\d+|[\w\+\-\/\* ]+)'

    monkey_rules = f.read().splitlines()

    monkeys = dict()
    for rule in monkey_rules:
        name, data = re.findall(PATTERN, rule)

        if data.isdigit():
            monkeys[name] = Monkey(data)
        else:
            dpndts = re.findall(r'(\w+)', data)

            monkeys[name] = Monkey(data, dpndts)

    def evaluate(monkey):
        if monkey.dependents is None:
            return int(monkey.operation)

        replacement_values = dict()
        for dep in monkey.dependents:
            replacement_values[dep] = evaluate(monkeys[dep])

        equation = monkey.operation
        for key, value in replacement_values.items():
            equation = equation.replace(key, str(value))
        return int(eval(equation))

    return evaluate(monkeys['root'])


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def partTwo(f: TextIOWrapper):
    PATTERN = r' ?(\d+|[\w\+\-\/\* ]+)'

    monkey_rules = f.read().splitlines()

    monkeys = dict()
    for rule in monkey_rules:
        name, data = re.findall(PATTERN, rule)

        if data.isdigit():
            monkeys[name] = Monkey(data)
        else:
            dpndts = re.findall(r'(\w+)', data)

            monkeys[name] = Monkey(data, dpndts)

    def buildTree(monkey):
        if monkey == monkeys['humn']:
            return Node('?')
        if monkey.dependents is None:
            return Node(int(monkey.operation))
        else:
            equation = monkey.operation.split(' ')
            l = buildTree(monkeys[equation[0]])
            r = buildTree(monkeys[equation[2]])
            return Node(equation[1], l, r)

    root = buildTree(monkeys['root'])

    def simplify(node: Node):
        if node.left is None:
            return Node(node.val)
        else:
            l = simplify(node.left)
            r = simplify(node.right)

            if type(l.val) != int or type(r.val) != int:
                return Node(node.val, l, r)

            if node.val == '+':
                val = l.val+r.val
            elif node.val == '-':
                val = l.val-r.val
            elif node.val == '*':
                val = l.val*r.val
            elif node.val == '/':
                val = l.val//r.val
            else:
                raise Exception(f'invalid operation is {node.val}')

            return Node(val)

    left_node = simplify(root.left)
    right_node = simplify(root.right)

    if type(left_node.val) != int:
        monkey_node = left_node
        goal = right_node.val
    else:
        monkey_node = right_node
        goal = left_node.val

    while monkey_node.val != goal:
        if monkey_node.val == '?':
            return goal

        left = monkey_node.left
        right = monkey_node.right

        if type(left.val) != int:
            monkey_is_left = True
        else:
            monkey_is_left = False

        if monkey_node.val == '+':
            if monkey_is_left:
                goal -= right.val
                monkey_node = left
            else:
                goal -= left.val
                monkey_node = right
        elif monkey_node.val == '-':
            if monkey_is_left:
                goal += right.val
                monkey_node = left
            else:
                goal = left.val - goal
                monkey_node = right
        elif monkey_node.val == '*':
            if monkey_is_left:
                goal = goal // right.val
                monkey_node = left
            else:
                goal = goal // left.val
                monkey_node = right
        elif monkey_node.val == '/':
            if monkey_is_left:
                goal = goal * right.val
                monkey_node = left
            else:
                goal = left.val // goal
                monkey_node = right


if __name__ == '__main__':
    with open('2022_21.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
