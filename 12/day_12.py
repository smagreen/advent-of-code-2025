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

def solve_region(w, h, present_ids, shapes):
    to_place = []
    for pid, count_val in enumerate(present_ids):
       for _ in range(count_val):
           to_place.append(pid)
    
    if not to_place: return True

    # Sort by size (area) descending
    to_place.sort(key=lambda pid: len(shapes[pid]), reverse=True)
    
    total_area = sum(len(shapes[pid]) for pid in to_place)
    if total_area > w * h:
        return False
        
    shapes_variants = {pid: get_variants(shapes[pid]) for pid in set(to_place)}
    occupied = set()
    
    def backtrack(idx):
        if idx == len(to_place):
            return True
            
        pid = to_place[idx]
        
        # Optimization: Try to place in first Available non-redundant spots? 
        # Standard backtracking iterates all positions.
        
        for variant, vw, vh in shapes_variants[pid]:
            # If present is larger than grid, skip
            if vw > w or vh > h: continue
            
            for y in range(h - vh + 1):
                for x in range(w - vw + 1):
                    # Check overlap
                    can_fit = True
                    for vx, vy in variant:
                        if (x + vx, y + vy) in occupied:
                            can_fit = False
                            break
                    
                    if can_fit:
                        # Place
                        new_cells = []
                        for vx, vy in variant:
                            p = (x + vx, y + vy)
                            occupied.add(p)
                            new_cells.append(p)
                        
                        if backtrack(idx + 1):
                            return True
                        
                        # Backtrack
                        for p in new_cells:
                            occupied.remove(p)
        return False

    return backtrack(0)

def part_1(filename):
    shapes, regions = parse_input(filename)
    count = 0
    for w, h, presents in regions:
        if solve_region(w, h, presents, shapes):
            count += 1
    return count

def part_2(filename):
    return 0

def main():
    """Main function to run the solution"""
    # Using 12/input.txt if it exists, otherwise test.txt for demonstration
    import os
    if os.path.exists('12/input.txt') and os.path.getsize('12/input.txt') > 0:
        file_to_use = '12/input.txt'
    else:
        file_to_use = '12/test.txt'
        
    print(f"Using {file_to_use}")
    print(f"Part 1 = {part_1(file_to_use)}")
    print(f"Part 2 = {part_2(file_to_use)}")

if __name__ == "__main__":
    main()
