#!/usr/bin/env python3
"""
Script to create a new Advent of Code day structure
Usage: python create_day.py <day_number>
"""

import sys
from pathlib import Path

def create_day(day_number):
    """Create directory structure and files for a new day"""
    # Create day directory
    day_dir = Path(f"{day_number}")
    day_dir.mkdir(exist_ok=True)
    # Create day_X.py
    day_file = day_dir / f"day_{day_number}.py"
    day_content = '''def read_input(filename):
    return [line.strip() for line in open(filename, 'r', encoding='utf-8')]

def part_1(data):
    # TODO: Implement part 1 solution
    return 0

def part_2(data):
    # TODO: Implement part 2 solution
    return 0

def main():
    """Main function to run the solution"""
    input_data = read_input('input.txt')
    print(f"Part 1 = {{part_1(input_data)}}")
    print(f"Part 2 = {{part_2(input_data)}}")

if __name__ == "__main__":
    main()
'''
    day_file.write_text(day_content)
    # Create test_day_X.py
    test_file = day_dir / f"test_day_{day_number}.py"
    test_content = f'''import pytest

# Import the functions from the same directory
from day_{day_number} import part_1, part_2

class TestDay{day_number}:
    
    def test_part_1_basic_cases(self):
        """Test part_1 with basic test cases"""
        # TODO: Add test cases when part_1 is implemented
        test_data = []  # Add sample data
        result = part_1(test_data)
        assert isinstance(result, int)
    
    def test_part_2_basic_cases(self):
        """Test part_2 with basic test cases"""
        # TODO: Add test cases when part_2 is implemented
        test_data = []  # Add sample data  
        result = part_2(test_data)
        assert isinstance(result, int)

# You can add fixtures for common test data
@pytest.fixture
def sample_input():
    """Sample input data for testing"""
    return [
        # TODO: Add sample data from puzzle description
    ]

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
'''
    test_file.write_text(test_content)
    # Create input.txt
    input_file = day_dir / "input.txt"
    input_content = (
        f"# Day {day_number} input will go here\n"
        "# Copy your actual puzzle input when you get it\n"
    )
    input_file.write_text(input_content)
    # Create test.txt
    test_input_file = day_dir / "test.txt"
    test_content_file = (
        f"# Test input for day {day_number}\n"
        "# Copy example data from the puzzle description\n"
    )
    test_input_file.write_text(test_content_file)
    print(f"✅ Created day {day_number} structure:")
    print(f"   📁 {day_dir}/")
    print(f"   📄 {day_file.name}")
    print(f"   🧪 {test_file.name}")
    print(f"   📝 {input_file.name}")
    print(f"   📝 {test_input_file.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_day.py <day_number>")
        sys.exit(1)

    try:
        day_num = int(sys.argv[1])
        if day_num < 1 or day_num > 25:
            print("Day number must be between 1 and 25")
            sys.exit(1)
        create_day(day_num)
    except ValueError:
        print("Day number must be an integer")
        sys.exit(1)
