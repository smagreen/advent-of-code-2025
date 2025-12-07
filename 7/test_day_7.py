import pytest

# Import the functions from the same directory
from day_7 import part_1, part_2, read_input

class TestDay7:
    
    def test_part_1_example(self):
        """Test part_1 with the example from test.txt"""
        test_data = read_input('7/test.txt')
        result = part_1(test_data)
        assert result == 21
    
    def test_part_2_example(self):
        """Test part_2 with the example from test.txt"""
        test_data = read_input('7/test.txt')
        result = part_2(test_data)
        assert result == 40

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
