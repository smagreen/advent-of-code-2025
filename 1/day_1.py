# pylint: disable=missing-module-docstring,missing-function-docstring

def read_input(filename):
    return [line.strip() for line in open(filename, 'r', encoding='utf-8')]

def part_1(data):
    position = 50
    count = 0
    for line in data:
        moves = int(line[1:]) * (-1 if line[0] == 'L' else 1)
        position = (position + moves) % 100
        if position == 0:
            count += 1
    return count

def part_2(data):
    position = 50
    count = 0
    for line in data:
        moves = int(line[1:]) * (-1 if line[0] == 'L' else 1)
        # Simulate the dial movement step by step
        remaining_moves = abs(moves)
        direction = 1 if moves > 0 else -1

        while remaining_moves > 0:
            # Move one step
            position = (position + direction) % 100
            remaining_moves -= 1

            # Check if we just hit zero
            if position == 0:
                count += 1

    return count

def main():
    """Main function to run the solution"""
    input_data = read_input('input.txt')
    print(f"Part 1 = { part_1(input_data) }")
    print(f"Part 2 = { part_2(input_data) }")

if __name__ == "__main__":
    main()
