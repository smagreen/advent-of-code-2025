import pytest

# Import the functions from the same directory
from day_4 import part_1, part_2, read_input

class TestDay4:
    
    def test_part_1_with_test_data(self):
        """Test part_1 with the test.txt data - should find 13 rolls with less than 4 adjacent rolls"""
        test_data = read_input('./4/test.txt')
        result = part_1(test_data)
        assert len(result) == 13, f"Expected 13 rolls, but found {len(result)}"
        assert isinstance(result, list)
        # Ensure all results are coordinate tuples
        for coord in result:
            assert isinstance(coord, tuple) and len(coord) == 2
    
    def test_part_1_empty_grid(self):
        """Test part_1 with empty grid"""
        test_data = []
        result = part_1(test_data)
        assert result == []
    
    def test_part_1_no_paper_rolls(self):
        """Test part_1 with grid containing no @ symbols"""
        test_data = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        result = part_1(test_data)
        assert result == []
    
    def test_part_1_single_roll(self):
        """Test part_1 with a single paper roll (should have 0 adjacent, so included)"""
        test_data = [
            ['.', '.', '.'],
            ['.', '@', '.'],
            ['.', '.', '.']
        ]
        result = part_1(test_data)
        assert result == [(1, 1)]
    
    def test_part_2_with_test_data(self):
        """Test part_2 with the test.txt data - iterative removal"""
        test_data = read_input('./4/test.txt')
        result = part_2(test_data)
        assert isinstance(result, int)
        assert result > 0, "Should remove some paper rolls"
        print(f"Part 2 removed {result} rolls total")
    
    def test_part_2_basic_cases(self):
        """Test part_2 with basic test cases"""
        # Test with small grid
        test_data = [
            ['.', '@', '.'],
            ['@', '@', '@'],
            ['.', '@', '.']
        ]
        result = part_2(test_data)
        # All @ symbols should be removed eventually
        assert result == 5

# You can add fixtures for common test data
@pytest.fixture
def sample_input():
    """Sample input data for testing"""
    return [
        ['@', '@', '.'],
        ['.', '@', '@'],
        ['@', '.', '.']
    ]

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
