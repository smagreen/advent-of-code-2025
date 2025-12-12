# pylint: disable=missing-module-docstring,missing-function-docstring
def read_input(filename):
    lines = [line.strip() for line in open(filename, 'r', encoding='utf-8')]
    return [tuple(map(int, line.split(','))) for line in lines if line.strip()]

def distance_2d(point1, point2):
    """Calculate Euclidean distance between two 2D points"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def part_1(points):
    max_area = 0
    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            x1, y1 = p1
            x2, y2 = p2
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            if width != height:
                area = width * height
                if area > max_area:
                    max_area = area
    return max_area

def part_2(points):
    from collections import defaultdict
    import math

    # 1. Identify Vertical Lines (Col Ranges)
    cols = defaultdict(list)
    for x, y in points:
        cols[x].append(y)
        
    col_intervals = []
    for x, ys in cols.items():
        if not ys: continue
        col_intervals.append((x, min(ys), max(ys)))
        
    if not col_intervals:
        return 0

    max_y_coord = max(p[1] for p in points)
    # Arrays to store GlobalLeft (min_bounds) and GlobalRight (max_bounds)
    sz = max_y_coord + 1
    min_bounds = [float('inf')] * sz
    max_bounds = [float('-inf')] * sz
    
    # Populate bounds
    for x, y_start, y_end in col_intervals:
        for y in range(y_start, y_end + 1):
            if x < min_bounds[y]:
                min_bounds[y] = x
            if x > max_bounds[y]:
                max_bounds[y] = x

    # Populate bounds
    for x, y_start, y_end in col_intervals:
        for y in range(y_start, y_end + 1):
            if x < min_bounds[y]: min_bounds[y] = x
            if x > max_bounds[y]: max_bounds[y] = x

    # Functional RMQ (Sparse Table)
    def build_st(arr, func):
        n = len(arr)
        if n == 0: return []
        k = int(math.log2(n))
        st = [[0] * (k + 1) for _ in range(n)]
        for i in range(n): st[i][0] = arr[i]
        for j in range(1, k + 1):
            length = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                st[i][j] = func(st[i][j-1], st[i + length][j-1])
        return st

    def query_st(st, L, R, func, default):
        if L > R or not st: return default
        j = int(math.log2(R - L + 1))
        return func(st[L][j], st[R - (1 << j) + 1][j])

    # We need max(min_bounds) <= L  => Build MAX table for min_bounds
    st_left_limit = build_st(min_bounds, max)
    
    # We need min(max_bounds) >= R  => Build MIN table for max_bounds
    st_right_limit = build_st(max_bounds, min)

    max_area = 0
    points_list = sorted(points) # Sort for determinism
    
    for i, p1 in enumerate(points_list):
        for p2 in points_list[i+1:]:
            x1, y1 = p1
            x2, y2 = p2
            
            if x1 == x2 or y1 == y2: continue
            
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            
            if width == height: continue
            
            L, R = min(x1, x2), max(x1, x2)
            T, B = min(y1, y2), max(y1, y2)
            
            # Validity Check via RMQ
            # max(min_bounds[T:B+1]) <= L
            left_valid = query_st(st_left_limit, T, B, max, float('-inf'))
            if left_valid > L:
                continue
                
            # min(max_bounds[T:B+1]) >= R
            right_valid = query_st(st_right_limit, T, B, min, float('inf'))
            if right_valid < R:
                continue
                
            area = width * height
            if area > max_area:
                max_area = area
                
    return max_area

def main():
    """Main function to run the solution"""
    input_data = read_input('9/input.txt')
    print(f"Part 1 = {part_1(input_data)}")
    print(f"Part 2 = {part_2(input_data)}")

if __name__ == "__main__":
    main()
