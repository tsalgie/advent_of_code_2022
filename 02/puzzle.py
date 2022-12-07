from typing import List

tie = {'A': 'X', 'B': 'Y', 'C': 'Z'}

def puzzle1(matches: List[str]) -> int:
    beat = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    scores = {'X': 1, 'Y': 2, 'Z': 3}    
    results = 0

    for match in matches:
        total = 0
        if tie[match[0]] == match[1]:
            total = 3
        elif beat[match[1]] == match[0]:
            total = 6

        results += total + scores[match[1]]

    return results

def puzzle2(matches: List[str]) -> int:
    beat = {'C': 'X', 'A': 'Y', 'B': 'Z'}
    lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}

    matches_copy = []   
    for match in matches:
        if match[1] == 'X':
            match[1] = lose[match[0]]
        elif match[1] == 'Y':
            match[1] = tie[match[0]]
        else:
            match[1] = beat[match[0]]
        matches_copy.append(match)

    return puzzle1(matches_copy)

if __name__ == "__main__":
    with open('input.txt') as f:
        matches = [line.split() for line in f.readlines()]

    print(puzzle1(matches))
    print(puzzle2(matches))
