import pytest
import os

# Import the functions from the same directory
from day_6 import read_input, part_1, part_2

class TestDay6:
    
    def test_part_1_basic_cases(self):
        """Test part_1 with test.txt example data"""
        # Test data from test.txt should give 4277556
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        data = read_input(test_file)
        result = part_1(data)
        assert result == 4277556
    
    def test_part_2_basic_cases(self):
        """Test part_2 with test.txt example data"""
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        result = part_2(test_file)
        assert result == 3263827

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
