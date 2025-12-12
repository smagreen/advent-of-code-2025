def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    parts = content.split('\n\n')
    
    shapes = {}
    regions = []
    
    for part in parts:
        lines = part.strip().split('\n')
        if not lines: continue
        header = lines[0].strip()
        
        if ':' in header and 'x' not in header.split(':')[0]: # Shape "0:"
            try:
                shape_id = int(header.split(':')[0])
                grid = lines[1:]
                points = set()
                for r, row in enumerate(grid):
                    for c, char in enumerate(row):
                        if char == '#':
                            points.add((c, r)) # x, y
                shapes[shape_id] = points
            except ValueError:
                pass 
        
        elif 'x' in header or 'x' in lines[0]: # Regions
            for line in lines:
                if ':' not in line: continue
                dims, counts = line.split(':')
                if 'x' not in dims: continue
                w, h = map(int, dims.strip().split('x'))
                presents = list(map(int, counts.strip().split()))
                regions.append((w, h, presents))
                
    return shapes, regions

def normalize(shape):
    if not shape: return frozenset()
    min_x = min(x for x,y in shape)
    min_y = min(y for x,y in shape)
    return frozenset((x - min_x, y - min_y) for x,y in shape)

def get_variants(shape):
    variants = set()
    current = list(shape)
    
    for _ in range(2): # Flip
        for _ in range(4): # Rotate
            variants.add(normalize(current))
            # Rotate 90 deg: (x, y) -> (-y, x)
            current = [(-y, x) for x, y in current]
        # Flip: (x, y) -> (-x, y)
        current = [(-x, y) for x, y in current]
        
    result = []
    for v in variants:
        if not v: continue
        w = max(x for x,y in v) + 1
        h = max(y for x,y in v) + 1
        result.append((v, w, h))
    # Sort variants by "compactness" or something? Just random is fine.
    return result

def solve_region(w, h, present_counts, shapes):
    # Prepare pieces: group by ID to handle duplicates efficiently
    import collections
    piece_counts = collections.defaultdict(int)
    for pid, count in enumerate(present_counts):
        if count > 0:
            piece_counts[pid] = count
        
    # Check total area constraints
    total_piece_area = 0
    for pid, count in piece_counts.items():
        total_piece_area += len(shapes[pid]) * count
        
    if total_piece_area > w * h:
        return False
    
    allowed_waste = (w * h) - total_piece_area
    
    # Precompute anchored variants for each piece type
    # Anchor: (min_y, min_x) becomes (0, 0)
    anchored_variants = {}
    for pid in piece_counts:
        variants = get_variants(shapes[pid])
        anchored_list = []
        for var, vw, vh in variants:
            # Re-normalize so first cell is (0,0)
            sorted_cells = sorted(list(var), key=lambda p: (p[1], p[0])) # sort by y, then x
            ay, ax = sorted_cells[0][1], sorted_cells[0][0]
            
            # Shift all
            shifted_var = []
            for vx, vy in var:
                shifted_var.append((vx - ax, vy - ay))
            anchored_list.append(shifted_var)
        anchored_variants[pid] = anchored_list

    # Grid state
    grid = [False] * (w * h)
    
    def solve(idx, waste_so_far):
        # Find next empty cell
        while idx < w * h and grid[idx]:
            idx += 1
            
        if idx == w * h:
            # Success if all pieces are used?
            # Actually, we track pieces used. If we reached end, we must check if all pieces used.
            # But simpler: if we successfully placed all pieces, we would have returned True earlier?
            # No, we recurse on grid index.
            # Check if any pieces left
            for c in piece_counts.values():
                if c > 0: return False # Should not happen if area check correct? 
                # Actually, waste skipping consumes indices without using pieces.
                # So we must verify all pieces are gone.
            return True
            
        # Optimization: If waste exceeded
        if waste_so_far > allowed_waste:
            return False
            
        x, y = idx % w, idx // w
        
        # Option 1: Try to place a piece here
        for pid in list(piece_counts.keys()): # List to avoid modification issues if we stored differently
            if piece_counts[pid] > 0:
                piece_counts[pid] -= 1
                
                # Try all variants
                for var in anchored_variants[pid]:
                    # Check fit
                    can_fit = True
                    placed_indices = []
                    for dx, dy in var:
                        nx, ny = x + dx, y + dy
                        nidx = ny * w + nx
                        
                        if not (0 <= nx < w and 0 <= ny < h): # Out of bounds
                            can_fit = False
                            break
                        if grid[nidx]: # Collision
                            can_fit = False
                            break
                        placed_indices.append(nidx)
                    
                    if can_fit:
                        # Place
                        for p_idx in placed_indices:
                            grid[p_idx] = True
                            
                        # Recurse
                        if solve(idx + 1, waste_so_far):
                            return True
                            
                        # Backtrack
                        for p_idx in placed_indices:
                            grid[p_idx] = False
                            
                piece_counts[pid] += 1
                
        # Option 2: Skip this cell (Gap)
        # Only allowed if we have waste budget
        if waste_so_far < allowed_waste:
            # Treat as filled (ignored)
            # grid[idx] is technically "False" but we skip it.
            # But the loop `while grid[idx]` needs it to be True or we manually skip.
            # Let's mark it True to skip it in next calls
            grid[idx] = True
            if solve(idx + 1, waste_so_far + 1):
                return True
            grid[idx] = False
            
        return False

    return solve(0, 0)

def part_1(filename):
    shapes, regions = parse_input(filename)
    count = 0
    for w, h, presents in regions:
        if solve_region(w, h, presents, shapes):
            count += 1
    return count

def main():
    """Main function to run the solution"""
    import sys
    sys.setrecursionlimit(3000) # Grid size up to 50x50 = 2500 cells recurse
    
    # Using 12/input.txt if it exists, otherwise test.txt for demonstration
    import os
    if os.path.exists('12/input.txt') and os.path.getsize('12/input.txt') > 0:
        file_to_use = '12/input.txt'
    else:
        file_to_use = '12/test.txt'
        
    print(f"Using {file_to_use}")
    print(f"Part 1 = {part_1(file_to_use)}")

if __name__ == "__main__":
    main()
