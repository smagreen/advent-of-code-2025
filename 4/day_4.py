def read_input(filename):
    """Read input file and return as 2D grid"""
    with open(filename, 'r', encoding='utf-8') as file:
        return [list(line.strip()) for line in file]

def part_1(data):
    """Find rolls of paper (@) with less than 4 adjacent paper rolls"""
    return find_removable_rolls(data)

def part_2(data):
    """Iteratively remove rolls of paper with less than 4 adjacent rolls"""
    if not data or not data[0]:
        return 0
    
    # Create a working copy of the grid
    grid = [row[:] for row in data]  # Deep copy
    total_removed = 0
    
    while True:
        # Find rolls to remove in this iteration
        rolls_to_remove = find_removable_rolls(grid)
        if not rolls_to_remove:
            break  # No more rolls to remove
        # Remove the rolls (set to '.')
        for x, y in rolls_to_remove:
            grid[y][x] = '.'
        
        total_removed += len(rolls_to_remove)
    
    return total_removed


def find_removable_rolls(grid):
    """Find rolls of paper (@) with less than 4 adjacent paper rolls"""
    if not grid or not grid[0]:
        return []
    
    rows = len(grid)
    cols = len(grid[0])
    result = []
    
    # Define 8 adjacent directions (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),           (0, 1),   # left, right
        (1, -1),  (1, 0),  (1, 1)    # bottom-left, bottom, bottom-right
    ]
    
    for y in range(rows):
        for x in range(cols):
            # Check if current position is a roll of paper
            if grid[y][x] == '@':
                # Count adjacent rolls of paper
                adjacent_count = 0
                
                for dy, dx in directions:
                    new_y = y + dy
                    new_x = x + dx
                    
                    # Check if the adjacent position is within bounds
                    if 0 <= new_y < rows and 0 <= new_x < cols:
                        if grid[new_y][new_x] == '@':
                            adjacent_count += 1
                
                # If less than 4 adjacent rolls, add to result
                if adjacent_count < 4:
                    result.append((x, y))
    
    return result

def main():
    """Main function to run the solution"""
    input_data = read_input('./4/input.txt')
    result = part_1(input_data)
    print(f"Part 1 = {len(result)} positions found")
    #print(f"Coordinates: {result}")
    print(f"Part 2 = {part_2(input_data)}")

if __name__ == "__main__":
    main()
