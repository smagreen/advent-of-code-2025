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

def part_2(data):
    return 0

def main():
    """Main function to run the solution"""
    input_data = read_input('9/input.txt')
    print(f"Part 1 = {part_1(input_data)}")
    print(f"Part 2 = {part_2(input_data)}")

if __name__ == "__main__":
    main()
