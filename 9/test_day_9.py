import pytest, os

# Import the functions from the same directory
from day_9 import read_input, part_1, part_2

class TestDay9:
    
    def test_part_1_basic_cases(self):
        """Test finding closest pair with test.txt data"""
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        data = read_input(test_file)
        area = part_1(data)
        assert isinstance(area, (int, float))        
        assert area == 50, f"Expected area 50, but got {area}"
    
    def test_part_2_basic_cases(self):
        """Test part_2 with basic test cases"""
        # TODO: Add test cases when part_2 is implemented
        test_data = []  # Add sample data  
        result = part_2(test_data)
        assert isinstance(result, int)

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
