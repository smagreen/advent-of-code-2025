import pytest
from day_2 import part_1, part_2, has_repeated_pattern

class TestDay2:
    """Test day 2 implementation"""
    
    def test_pattern_detection_exact_twice(self):
        """Test has_repeated_pattern with exact_twice=True"""
        # Should match patterns repeated exactly twice
        assert has_repeated_pattern("55", exact_twice=True)  # 5 twice
        assert has_repeated_pattern("6464", exact_twice=True)  # 64 twice  
        assert has_repeated_pattern("123123", exact_twice=True)  # 123 twice
        assert has_repeated_pattern("12341234", exact_twice=True)  # 1234 twice
        
        # Should not match single digits or more than twice
        assert not has_repeated_pattern("5", exact_twice=True)
        assert not has_repeated_pattern("555", exact_twice=True)  # 5 three times (not exactly twice)
        assert not has_repeated_pattern("123", exact_twice=True)  # no repetition

    def test_pattern_detection_at_least_twice(self):
        """Test has_repeated_pattern with exact_twice=False"""
        # Should match patterns repeated at least twice
        assert has_repeated_pattern("55", exact_twice=False)  # 2 times
        assert has_repeated_pattern("555", exact_twice=False)  # 3 times
        assert has_repeated_pattern("6464", exact_twice=False)  # 2 times
        assert has_repeated_pattern("646464", exact_twice=False)  # 3 times
        
        # Should not match single occurrence
        assert not has_repeated_pattern("5", exact_twice=False)
        assert not has_repeated_pattern("123", exact_twice=False)

    def test_parts_return_integers(self):
        """Test both parts return integers for empty data"""
        test_data = []
        
        assert isinstance(part_1(test_data), int)
        assert isinstance(part_2(test_data), int)

    def test_parts_with_sample_ranges(self):
        """Test both parts with sample ranges"""
        test_data = [(10, 99), (1000, 1100)]  # Sample ranges
        
        result_1 = part_1(test_data)
        result_2 = part_2(test_data)
        
        # Should find some invalid numbers and return positive integers
        assert isinstance(result_1, int) and result_1 >= 0
        assert isinstance(result_2, int) and result_2 >= 0
        # Part 2 should be >= Part 1 (at least twice includes exactly twice)
        assert result_2 >= result_1

if __name__ == "__main__":
    pytest.main([__file__, "-v"])