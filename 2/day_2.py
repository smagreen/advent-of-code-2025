import re

def read_input(filename):
    """Read ranges from input file"""
    lines = [line.strip() for line in open(filename, 'r', encoding='utf-8')]
    ranges = lines[0].split(',') if lines else []
    return [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges if '-' in r]

def has_repeated_pattern(num_str, exact_twice=True):
    """Check if number has repeated digit patterns"""
    if exact_twice:
        # Part 1: exactly twice - simple regex
        return bool(re.match(r'^(\d+)\1$', num_str))
    
    # Part 2: at least twice - check all possible pattern lengths
    for length in range(1, len(num_str) // 2 + 1):
        pattern = num_str[:length]
        if num_str == pattern * (len(num_str) // length) and len(num_str) // length >= 2:
            return True
    return False

def find_invalid_sum(ranges, exact_twice=True):
    """Find sum of invalid numbers in ranges"""
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            if has_repeated_pattern(str(num), exact_twice):
                total += num
    return total

def part_1(data):
    """Sum of numbers with patterns repeated exactly twice"""
    return find_invalid_sum(data, exact_twice=True)

def part_2(data):
    """Sum of numbers with patterns repeated at least twice"""
    return find_invalid_sum(data, exact_twice=False)

def main():
    """Main function"""
    data = read_input('input.txt')
    print(f"Part 1 = {part_1(data)}")
    print(f"Part 2 = {part_2(data)}")

if __name__ == "__main__":
    main()
