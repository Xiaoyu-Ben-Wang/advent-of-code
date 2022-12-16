from importlib.resources import path
from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import re


index = 0
def partOne(f: TextIOWrapper):
    PATTERN = r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)'

    connection_map = dict()
    flow_map = dict()
    for line in f.readlines():
        valve, flow, connections = re.findall(PATTERN, line.strip())[0]
        flow = int(flow)
        connections = [c.strip() for c in connections.split(',')]

        connection_map[valve] = connections
        flow_map[valve] = flow

    dp = dict()

    def solve(position: str, remaining_steps: int, opened: set):
        if remaining_steps == 0:
            return 0
        if (position, remaining_steps, tuple(sorted(opened))) in dp:
            return dp[(position, remaining_steps, tuple(sorted(opened)))]
        
        # list of values that we can choose from
        possible_values = []
        if position not in opened and flow_map[position] != 0:
            # choose to open
            new_opened = opened.copy()
            new_opened.add(position)
            possible_values.append(flow_map[position] * (remaining_steps-1)+solve(position, remaining_steps-1, new_opened))
        
        for next_pos in connection_map[position]:
            possible_values.append(solve(next_pos, remaining_steps-1, opened ))
        


        dp[(position, remaining_steps, tuple(sorted(opened)))] = max(possible_values)
        return max(possible_values)
    
    return solve('AA', 30, set())


def partTwo(f: TextIOWrapper):
    PATTERN = r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)'

    connection_map = dict()
    flow_map = dict()
    for line in f.readlines():
        valve, flow, connections = re.findall(PATTERN, line.strip())[0]
        flow = int(flow)
        connections = [c.strip() for c in connections.split(',')]

        connection_map[valve] = connections
        flow_map[valve] = flow

    dp = dict()

    def solve(elf: str, elephant:str, remaining_steps: int, opened: set):
        if remaining_steps == 0:
            return 0
        if (elf, elephant, remaining_steps, tuple(sorted(opened))) in dp:
            return dp[(elf, elephant, remaining_steps, tuple(sorted(opened)))]
        
        # list of values that we can choose from
        possible_values = []
        if elf not in opened and flow_map[elf] != 0:
            new_opened = opened.copy()
            # choose to open
            new_opened.add(elf)
            res = solve(position, remaining_steps-1, new_opened)
            possible_values.append((flow_map[position] * (remaining_steps-1)+res[0], res[1]))
        
        for next_pos in connection_map[position]:
            possible_values.append(solve(next_pos, remaining_steps-1, opened ))
        


        dp[(position, remaining_steps, tuple(sorted(opened)))] = max(possible_values)[0]
        return max(possible_values, key=lambda x: x[0])
    
    elf = solve('AA', 26, set())

    return elf[0]+elephant[0] 


if __name__ == '__main__':
    with open('2022_16.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')