def apply_operation(numbers, operation):
    """Apply operation to list of numbers"""
    if operation == '+':
        return sum(numbers)
    result = 1
    for num in numbers:
        result *= num
    return result

def read_input(filename):
    """Read input file with columns of integers and operations in last row"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    rows = [line.split() for line in lines]
    operations = rows[-1]
    number_rows = rows[:-1]
    
    # Group by columns and pair with operations
    return [([int(row[i]) for row in number_rows if i < len(row)], operations[i]) 
            for i in range(len(operations))]

def part_1(data):
    """Calculate sum or product for each column based on operation"""
    return sum(apply_operation(numbers, op) for numbers, op in data)

def part_2(filename):
    """Extract digits by character position using operator positions as boundaries"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n\r') for line in f]
    
    ops_line = lines[-1]
    data_lines = lines[:-1]
    
    # Find operator positions - these mark column left boundaries
    op_positions = [i for i, c in enumerate(ops_line) if c in '+*']
    operations = [ops_line[i] for i in op_positions]
    # Use max length of data lines for the right boundary
    max_len = max(len(line) for line in data_lines) if data_lines else len(ops_line)
    op_positions.append(max_len)
    
    total = 0
    # Process columns right-to-left
    for col_idx in range(len(operations) - 1, -1, -1):
        left, right = op_positions[col_idx], op_positions[col_idx + 1]
        operation = operations[col_idx]
        
        # Process positions right to left within column, extract digits top to bottom
        position_numbers = []
        for pos in range(right - 1, left - 1, -1):
            digits = [line[pos] for line in data_lines if pos < len(line) and line[pos].isdigit()]
            if digits:
                position_numbers.append(int(''.join(digits)))
        
        total += apply_operation(position_numbers, operation)
    
    return total

def main():
    """Main function to run the solution"""
    data = read_input('input.txt')
    print(f"Part 1 = {part_1(data)}")
    print(f"Part 2 = {part_2('input.txt')}")

if __name__ == "__main__":
    main()
