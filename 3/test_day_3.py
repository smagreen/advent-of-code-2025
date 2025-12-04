# pylint: disable=missing-module-docstring,missing-function-docstring, missing-class-docstring
import pytest

# Import the functions from the same directory
from day_3 import part_1, part_2

class TestDay3:
    def test_part_1_basic_cases(self):
        """Test part_1 with basic test cases"""
        test_banks = [987654321111111,
            811111111111119,
            234234234234278,
            818181911112111
        ]
        result = part_1(test_banks)
        assert isinstance(result, int)
        # Add specific assertions based on expected results
        assert result == 357

    def test_part_2_basic_cases(self):
        """Test part_2 with basic test cases"""
        test_banks = [987654321111111,
            811111111111119,
            234234234234278,
            818181911112111
        ]
        result = part_2(test_banks)
        assert isinstance(result, int)
        # Add specific assertions based on expected results
        assert result == 3121910778619

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])
