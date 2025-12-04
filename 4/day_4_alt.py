def read_input(filename):
    """Read input file and return as 2D grid"""
    with open(filename, 'r', encoding='utf-8') as file:
        return [list(line.strip()) for line in file]

def get_paper_rolls(grid):
    """Extract paper roll coordinates from grid"""
    rolls = set()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                rolls.add((x, y))
    return rolls, len(grid[0]) if grid and grid[0] else 0, len(grid)

def count_adjacent(x, y, rolls, max_x, max_y):
    """Count adjacent paper rolls for a given position"""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(1 for dx, dy in directions 
               if 0 <= x + dx < max_x and 0 <= y + dy < max_y and (x + dx, y + dy) in rolls)

def find_removable(rolls, max_x, max_y):
    """Find rolls with less than 4 adjacent rolls"""
    return [pos for pos in rolls if count_adjacent(*pos, rolls, max_x, max_y) < 4]

def part_1(data):
    """Find rolls of paper (@) with less than 4 adjacent paper rolls"""
    rolls, max_x, max_y = get_paper_rolls(data)
    return find_removable(rolls, max_x, max_y)

def part_2(data):
    """Iteratively remove rolls of paper with less than 4 adjacent rolls"""
    rolls, max_x, max_y = get_paper_rolls(data)
    total_removed = 0
    
    while rolls:
        to_remove = find_removable(rolls, max_x, max_y)
        if not to_remove:
            break
        for pos in to_remove:
            rolls.discard(pos)
        total_removed += len(to_remove)
    
    return total_removed

def main():
    """Main function to run the solution"""
    input_data = read_input('./4/input.txt')
    print(f"Part 1 = {len(part_1(input_data))} positions found")
    print(f"Part 2 = {part_2(input_data)}")

if __name__ == "__main__":
    main()