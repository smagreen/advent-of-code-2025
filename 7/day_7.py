def read_input(filename):
    return [line.strip() for line in open(filename, 'r', encoding='utf-8')]

def part_1(data):
    # Find starting position
    start_col = None
    for col, char in enumerate(data[0]):
        if char == 'S':
            start_col = col
            break
    
    # Track active beams
    active_beams = {start_col}
    split_count = 0
    
    # Process row by row
    for row_idx in range(1, len(data)):
        row = data[row_idx]
        new_beams = set()
        
        for col in active_beams:
            # Check if beam hits a splitter at this position
            if col < len(row) and row[col] == '^':
                # Count this split event
                split_count += 1
                
                # Beam splits into left and right
                if col - 1 >= 0:
                    new_beams.add(col - 1)
                if col + 1 < len(row):
                    new_beams.add(col + 1)
            else:
                # Beam continues down
                new_beams.add(col)
        
        active_beams = new_beams
    
    return split_count

def part_2(data):
    # Find starting position
    start_col = None
    for col, char in enumerate(data[0]):
        if char == 'S':
            start_col = col
            break
    
    # Cache for memoization: (row, col) -> number of paths from that position
    cache = {}
    
    def count_paths(row, col):
        """Count all possible paths from (row, col) to the bottom of the grid"""
        # Base case: reached the bottom
        if row >= len(data):
            return 1
        
        # Check cache
        if (row, col) in cache:
            return cache[(row, col)]
        
        # Check if current position has a splitter
        if col < len(data[row]) and data[row][col] == '^':
            # Split into two paths
            total_paths = 0
            
            # Left path
            if col - 1 >= 0:
                total_paths += count_paths(row + 1, col - 1)
            
            # Right path
            if col + 1 < len(data[row]):
                total_paths += count_paths(row + 1, col + 1)
            
            cache[(row, col)] = total_paths
            return total_paths
        else:
            # Continue straight down
            result = count_paths(row + 1, col)
            cache[(row, col)] = result
            return result
    
    return count_paths(0, start_col)

def main():
    """Main function to run the solution"""
    input_data = read_input('input.txt')
    print(f"Part 1 = {part_1(input_data)}")
    print(f"Part 2 = {part_2(input_data)}")

if __name__ == "__main__":
    main()
