from typing import List

def puzzle(calories: List[int], elf_count: int = 1) -> int:
    return sum(sorted(calories)[-elf_count:])

if __name__ == "__main__":
    with open('input.txt') as f:
        calories = [sum(map(int, group.split('\n'))) for group in f.read().split('\n\n')]

    print(puzzle(calories))
    print(puzzle(calories, 3))
