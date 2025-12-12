import pytest
import os
from day_10 import part_1, part_2, read_input

class TestDay10:
    
    def test_part_1_example(self):
        """Test part_1 with the provided example in test.txt"""
        # Read the test file directly using absolute path relative to this file
        test_file_path = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_data = read_input(test_file_path)
        result = part_1(test_data)
        assert result == 7
    
    def test_part_2_example(self):
        """Test part_2 with the provided example in test.txt"""
        # Read the test file directly using absolute path relative to this file
        test_file_path = os.path.join(os.path.dirname(__file__), 'test.txt')
        test_data = read_input(test_file_path)
        result = part_2(test_data)
        assert result == 33

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
