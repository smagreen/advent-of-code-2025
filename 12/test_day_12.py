import pytest, os

# Import the functions from the same directory
from day_12 import part_1

class TestDay12:
    
    def test_part_1_basic_cases(self):
        """Test part_1 with test.txt data"""
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        result = part_1(test_file)
        assert result == 2, f"Expected 2, but got {result}"
    


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
