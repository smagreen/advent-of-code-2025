def read_input(filename):
    """Read input file with two sections separated by blank line"""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    
    # Find the blank line separator
    blank_line = lines.index('')
    
    # Parse ranges (first section)
    ranges = [tuple(map(int, line.split('-'))) for line in lines[:blank_line]]
    
    # Parse integers (second section)
    numbers = [int(line) for line in lines[blank_line + 1:]]
    
    return ranges, numbers

def merge_overlapping_ranges(ranges):
    """Merge overlapping ranges into a set of non-overlapping ranges"""
    if not ranges:
        return []
    
    # Sort ranges by start value
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    
    for current in sorted_ranges[1:]:
        last = merged[-1]
        # If ranges overlap or are adjacent, merge them
        if current[0] <= last[1] + 1:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    return merged

def part_1(data):
    """Count integers that fall within any range"""
    ranges, numbers = data
    return sum(1 for number in numbers 
               if any(low <= number <= high for low, high in ranges))

def part_2(data):
    """Count unique numbers within all merged ranges"""
    ranges, _ = data
    merged_ranges = merge_overlapping_ranges(ranges)
    return sum(high - low + 1 for low, high in merged_ranges)

def main():
    """Main function to run the solution"""
    data = read_input('input.txt')
    print(f"Part 1 = {part_1(data)}")
    print(f"Part 2 = {part_2(data)}")

if __name__ == "__main__":
    main()
