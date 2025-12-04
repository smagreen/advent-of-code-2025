# pylint: disable=missing-module-docstring,missing-function-docstring, missing-class-docstring

# Import the functions from the same directory
import os
import sys

import pytest
from day_1 import part_1, part_2

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

class TestDay1:

    def test_part_1_basic_cases(self):
        """Test part_1 with basic test cases"""
        # Test case: should land on 0
        test_data = ["R50"]  # Start at 50, move right 50 -> land at 0
        assert part_1(test_data) == 1
        # Test case: should not land on 0
        test_data = ["R30"]  # Start at 50, move right 30 -> land at 80
        assert part_1(test_data) == 0
        # Test case: multiple moves with one landing on 0
        test_data = ["R30", "L80"]  # 50->80->0
        assert part_1(test_data) == 1

    def test_part_1_wraparound(self):
        """Test part_1 with wraparound cases"""
        # Test wraparound to 0
        test_data = ["R150"]  # Start at 50, move right 150 -> (50+150)%100 = 0
        assert part_1(test_data) == 1
        # Test left wraparound to 0
        test_data = ["L50"]  # Start at 50, move left 50 -> (50-50)%100 = 0
        assert part_1(test_data) == 1

    def test_part_2_single_crossing(self):
        """Test part_2 with single zero crossings"""
        # Test simple right crossing
        test_data = ["R60"]  # Start at 50, move right 60 -> crosses 0 once
        assert part_2(test_data) == 1

        # Test simple left crossing
        test_data = ["L60"]  # Start at 50, move left 60 -> crosses 0 once
        assert part_2(test_data) == 1

        # Test no crossing
        test_data = ["R30"]  # Start at 50, move right 30 -> no zero crossing
        assert part_2(test_data) == 0

    def test_part_2_multiple_crossings(self):
        """Test part_2 with multiple zero crossings in one move"""
        # Test multiple crossings - step by step simulation shows 3 crossings for R250
        test_data = ["R250"]  # Start at 50, step-by-step shows 3 crossings
        result = part_2(test_data)
        assert result == 3  # Updated based on actual step-by-step simulation

        # Test large left move
        test_data = ["L150"]  # Step-by-step simulation shows 2 crossings
        assert part_2(test_data) == 2

    def test_part_2_edge_cases(self):
        """Test part_2 edge cases"""
        # Test move that doesn't cross zero
        test_data = ["R49"]  # Start at 50, end at 99 - no crossing
        assert part_2(test_data) == 0
        # Test minimal crossing
        test_data = ["R51"]  # Start at 50, end at 1 - crosses 0 once
        assert part_2(test_data) == 1


# You can add fixtures for common test data
@pytest.fixture
def sample_input():
    """Sample input data for testing"""
    return [
        "R10",
        "L5",
        "R20",
        "L15"
    ]


class TestIntegration:
    def test_with_sample_data(self):
        """Test both parts with sample data"""
        test_data = ["R10", "L5", "R20", "L15"]
        result1 = part_1(test_data)
        result2 = part_2(test_data)
        # Add assertions based on expected results
        assert isinstance(result1, int)
        assert isinstance(result2, int)
        assert result2 >= result1  # part_2 should generally be >= part_1

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
