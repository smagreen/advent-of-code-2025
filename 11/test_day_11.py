import pytest, os

# Import the functions from the same directory
from day_11 import part_1, part_2, read_input

class TestDay11:
    
    def test_part_1_basic_cases(self):
        """Test counting paths with test.txt data"""
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        graph = read_input(test_file)
        result = part_1(graph)
        assert result == 5, f"Expected 5, but got {result}"
    
    def test_part_2_basic_cases(self):
        """Test part_2 with basic test cases"""
        # TODO: Add test cases when part_2 is implemented
        pass

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
