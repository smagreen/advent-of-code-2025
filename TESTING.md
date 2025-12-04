# Testing for Advent of Code

This project uses **pytest** as the testing framework (equivalent to Jest for JavaScript).

## Running Tests

```bash
# Run all tests
python -m pytest

# Run tests with verbose output
python -m pytest -v

# Run specific test file
python -m pytest test_day_1.py

# Run specific test method
python -m pytest test_day_1.py::TestDay1::test_part_1_basic_cases

# Run tests with coverage (if pytest-cov is installed)
python -m pytest --cov=day_1
```

## Test Structure

- `test_*.py` files contain test cases
- Classes starting with `Test*` group related tests
- Functions starting with `test_*` are individual test cases
- Use `assert` statements for validation
- `@pytest.fixture` decorator creates reusable test data

## Key Testing Concepts

### Assertions
```python
assert result == expected_value
assert len(data) > 0
assert "error" in error_message
```

### Fixtures (like Jest beforeEach)
```python
@pytest.fixture
def sample_data():
    return ["R10", "L20", "R30"]

def test_something(sample_data):
    result = part_1(sample_data)
    assert result == 1
```

### Parametrized Tests
```python
@pytest.mark.parametrize("input_data,expected", [
    (["R50"], 1),
    (["R30"], 0),
    (["L50"], 1),
])
def test_part_1_cases(input_data, expected):
    assert part_1(input_data) == expected
```

### Test Organization
```python
class TestPart1:
    def test_basic_cases(self):
        # Test basic functionality
        pass
    
    def test_edge_cases(self):
        # Test boundary conditions
        pass
    
    def test_error_handling(self):
        # Test error scenarios
        pass
```

## Benefits over Manual Testing

1. **Automated**: Run all tests with one command
2. **Regression Prevention**: Catch breaking changes
3. **Documentation**: Tests show expected behavior
4. **Confidence**: Refactor safely knowing tests will catch issues
5. **Fast Feedback**: Immediate results during development