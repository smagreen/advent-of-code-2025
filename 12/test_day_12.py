import pytest

# Import the functions from the same directory
from day_12 import part_1, part_2

class TestDay12:
    
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
