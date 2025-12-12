import re
from collections import deque

def read_input(filename):
    return [line.strip() for line in open(filename, 'r', encoding='utf-8') if line.strip()]

def parse_line(line):
    # Extract light count and target from [...]
    match_lights = re.search(r'\[(.*?)\]', line)
    if not match_lights:
        return 0, 0, [], []
    
    light_str = match_lights.group(1)
    num_lights = len(light_str)
    
    # Parse target state (Part 1 input)
    target_state = 0
    for i, char in enumerate(light_str):
        if char == '#':
            target_state |= (1 << i)
            
    # Parse target counters (Part 2 input) from {...}
    target_counters = []
    match_counters = re.search(r'\{(.*?)\}', line)
    if match_counters:
         target_counters = [int(x.strip()) for x in match_counters.group(1).split(',')]
    
    # Extract buttons from (...)
    # Find all occurrences of (...)
    buttons = []
    matches_buttons = re.findall(r'\((.*?)\)', line)
    for m in matches_buttons:
        if not m.strip():
            continue
        parts = [int(x.strip()) for x in m.split(',')]
        # Create bitmask for button
        mask = 0
        for p in parts:
            if 0 <= p < num_lights:
                mask |= (1 << p)
        buttons.append(mask)
        
    return num_lights, target_state, target_counters, buttons

def solve_puzzle(num_lights, buttons, target_state):
    start_state = 0
    
    if start_state == target_state:
        return 0

    queue = deque([(start_state, 0)])
    visited = {start_state}
    
    while queue:
        current_state, presses = queue.popleft()
        
        if current_state == target_state:
            return presses
            
        for button_mask in buttons:
            next_state = current_state ^ button_mask
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, presses + 1))
                
    return 0 # Should ideally not happen if solvable per problem description

def solve_linear(num_lights, buttons, target_counters):
    # System A * x = b
    # A has rows = num_lights, cols = num_buttons
    
    num_vars = len(buttons)
    num_eqs = num_lights
    
    # Build matrix
    matrix = []
    for r in range(num_eqs):
        row = []
        for c in range(num_vars):
            # Check if button c affects light r
            val = 1 if (buttons[c] >> r) & 1 else 0
            row.append(val)
        matrix.append(row)
        
    b_vec = list(target_counters)
    
    # Gaussian elimination to find RREF
    pivots = {} # col -> row
    free_vars = []
    
    # Forward elimination
    pivot_row = 0
    col = 0
    augmented = [row[:] + [b_vec[i]] for i, row in enumerate(matrix)]
    
    while pivot_row < num_eqs and col < num_vars:
        # Find pivot
        sel = -1
        for r in range(pivot_row, num_eqs):
            if abs(augmented[r][col]) > 1e-9:
                sel = r
                break
        
        if sel == -1:
            free_vars.append(col)
            col += 1
            continue
            
        # Swap
        augmented[pivot_row], augmented[sel] = augmented[sel], augmented[pivot_row]
        pivots[col] = pivot_row
        
        # Normalize
        factor = augmented[pivot_row][col]
        for c in range(col, num_vars + 1):
            augmented[pivot_row][c] /= factor
            
        # Eliminate others
        for r in range(num_eqs):
            if r != pivot_row and abs(augmented[r][col]) > 1e-9:
                f = augmented[r][col]
                for c in range(col, num_vars + 1):
                    augmented[r][c] -= f * augmented[pivot_row][c]
                    
        pivot_row += 1
        col += 1
        
    # Add remaining cols as free vars
    for c in range(col, num_vars):
        if c not in pivots:
            free_vars.append(c)

    # Check consistency
    for r in range(pivot_row, num_eqs):
        if abs(augmented[r][-1]) > 1e-9:
            return 0 # Inconsistent system
            
    # Solve by iterating free variables or using ILP
    # Since we want minimum sum of k_i >= 0
    # k_pivot = b'_pivot - sum(k_free * A'_free)
    
    best_sum = float('inf')
    
    # Heuristic limit for free vars search space based on max target
    # If free vars are small, this works. The problem might have multiple solutions.
    # Given the puzzle type, maybe we can assume small coefficients?
    # Actually, iterate free variables from 0 to some limit?
    # Max target is ~300. 
    import itertools
    
    limit = max(target_counters) + 2 if target_counters else 5
    
    # If too many free vars, this is still slow, but usually only 1-3
    if len(free_vars) > 4:
         # Fallback to optimization?
         limit = 50 # Heuristic limit
         
    def check(free_vals):
        current_sum = sum(free_vals)
        sol = [0] * num_vars
        
        # Set free vars
        for fv, val in zip(free_vars, free_vals):
            sol[fv] = val
            
        # Calc pivot vars
        valid = True
        for col in range(num_vars - 1, -1, -1):
            if col in free_vars:
                continue
            
            row = pivots[col]
            # val = rhs - sum(coeff * known_val)
            val = augmented[row][-1]
            for c in range(col + 1, num_vars):
                val -= augmented[row][c] * sol[c]
                
            # Check integer and non-negative
            if val < -1e-9 or abs(val - round(val)) > 1e-9:
                valid = False
                break
            sol[col] = int(round(val))
            current_sum += sol[col]
            
        return current_sum if valid else float('inf')

    # Optimization: Iterate sum of free vars first?
    # Simple bounds: 0 to limit
    ranges = [range(limit) for _ in free_vars]
    
    # If no free vars
    if not free_vars:
        s = check([])
        return s if s != float('inf') else 0

    for combo in itertools.product(*ranges):
        s = check(combo)
        if s < best_sum:
            best_sum = s
            
    return best_sum if best_sum != float('inf') else 0

def solve_part2(num_lights, buttons, target_counters):
    return solve_linear(num_lights, buttons, target_counters)

def part_1(data):
    total_presses = 0
    for line in data:
        num_lights, target, _, buttons = parse_line(line)
        if num_lights > 0:
            presses = solve_puzzle(num_lights, buttons, target)
            total_presses += presses
    return total_presses

def part_2(data):
    total_presses = 0
    for line in data:
        num_lights, _, target_counters, buttons = parse_line(line)
        if num_lights > 0 and target_counters:
            presses = solve_part2(num_lights, buttons, target_counters)
            total_presses += presses
    return total_presses

def main():
    """Main function to run the solution"""
    try:
        input_data = read_input('input.txt')
        print(f"Part 1 = {part_1(input_data)}")
        print(f"Part 2 = {part_2(input_data)}")
    except FileNotFoundError:
        print("input.txt not found. Running tests only.")

if __name__ == "__main__":
    main()
