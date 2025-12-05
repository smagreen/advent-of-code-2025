import pytest

# Import the functions from the same directory
from day_5 import part_1, part_2

class TestDay5:
    
    def test_part_1_basic_cases(self):
        """Test part_1 with test.txt example data"""
        # Test data from test.txt
        ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
        numbers = [1, 5, 8, 11, 17, 32]
        test_data = (ranges, numbers)
        
        result = part_1(test_data)
        # Should return count of numbers (5, 11, 17) that fall within ranges = 3
        assert result == 3
    
    def test_part_2_basic_cases(self):
        """Test part_2 with test.txt example data"""
        # Test data from test.txt
        ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]
        numbers = [1, 5, 8, 11, 17, 32]
        test_data = (ranges, numbers)
        
        result = part_2(test_data)
        # Merged ranges: (3,5) has 3 numbers, (10,20) has 11 numbers = 14 total
        assert result == 14

# You can add fixtures for common test data
@pytest.fixture
def sample_input():
    """Sample input data for testing"""
    return []

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
