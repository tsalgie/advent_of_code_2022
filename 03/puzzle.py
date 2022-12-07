from typing import List

def puzzle1(lines: List[str]) -> int:
    total = 0
    for line in lines:
        c = common(line)
        p = priority(c)
        total += p

    return total   

def puzzle2(lines: List[str]) -> int:
    total = 0
    for i in range(0, len(lines), 3):
        chunk = lines[i:i+3]
        c = common2(chunk)
        p = priority(c)
        total += p

    return total      

def priority(item_type: str) -> int:
    val = ord(item_type) - 96
    val = val if val > 0 else val + 58
    return val

def common(line: str) -> str:
    n = int(len(line)/2)
    s = set(line[:n]).intersection(line[n:])
    return next(iter(s))

def common2(lines: List[str]) -> str:
    s = set(lines[0].strip()).intersection(lines[1].strip()).intersection(lines[2].strip())
    return next(iter(s))

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
    
    print(puzzle1(lines))
    print(puzzle2(lines))
