def puzzle(datastream: str, marker_size: int) -> int:
    for i in range(marker_size, len(datastream)):
        if len(set(datastream[i - marker_size:i])) == marker_size:
            return(i)

if __name__ == "__main__":
    with open('input.txt') as f:
        datastream = f.read().strip()
    print(puzzle(datastream, 4))
    print(puzzle(datastream, 14))
