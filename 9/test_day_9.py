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
        # Rectangle 10x5 (0-10, 0-5) -> Area 11*6 = 66
        # Both L-paths exist here if we define connectivity carefully.
        # But my synthetic test was assuming simplistic connectivity.
        # Let's adjust synthetic test to "Full Connectivity" to be safe?
        # A simple rect (0,0), (10,0), (0,5), (10,5) has full connectivity.
        data = [(0,0), (10,0), (0,5), (10,5)]
        assert part_2(data) == 66
        
        # Square is ignored
        data_sq = [(0,0), (10,0), (0,10), (10,10)]
        assert part_2(data_sq) == 0

    def test_part_2_file_example(self):
        """Test finding largest rect in test.txt"""
        test_file = os.path.join(os.path.dirname(__file__), 'test.txt')
        data = read_input(test_file)
        area = part_2(data)
        assert area == 24, f"Expected area 24, but got {area}"

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
