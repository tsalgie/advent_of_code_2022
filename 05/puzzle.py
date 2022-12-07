from typing import List

def puzzle(moves: List[str], state: List[List[str]], order_move: bool = False) -> str:
    for move in moves:
        items = move.strip().split()
        num = int(items[1])
        source = int(items[3]) - 1
        dest = int(items[5]) - 1
        state[dest] += state[source][-num:] if order_move else reversed(state[source][-num:])
        state[source] = state[source][:-num]

    return ''.join([s[-1] for s in state])


if __name__ == "__main__":
    with open('input.txt') as f:
        parts = f.read().split('\n\n')
    state_lines = parts[0].split('\n')
    state = []
    for i in range(1, len(state_lines[0]), 4):
        s = list(reversed([*''.join([line[i] for line in state_lines]).strip()][:-1]))
        state.append(s)
    moves = parts[1].split('\n')

    print(puzzle(moves, [i.copy() for i in state]))
    print(puzzle(moves, state, True))
