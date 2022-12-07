import re
from typing import Callable, List

def puzzle(lines: List[str], solver: Callable) -> int:
    total = 0
    for line in lines:
        ranges = re.split(',|-', line)
        r1 = set(range(int(ranges[0]), int(ranges[1]) + 1))
        r2 = set(range(int(ranges[2]), int(ranges[3]) + 1))
        total += 1 if solver(r1, r2) else 0

    return total

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    s1 = lambda x, y: len(x.intersection(y)) == len(x) or len(x.intersection(y)) == len(y)
    s2 = lambda x, y: len(x.intersection(y)) > 0

    print(puzzle(lines, s1))
    print(puzzle(lines, s2))
