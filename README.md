# Advent of Code 2025 🎄

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) implemented in Python.

## Structure

Each day has its own directory with:
- `day_X.py` - Main solution file
- `test_day_X.py` - Test cases
- `input.txt` - Puzzle input (not tracked in git)
- `test.txt` - Sample test data from puzzle descriptions

```
advent-of-code-2025/
├── 1/
│   ├── day_1.py
│   └── test_day_1.py
├── 2/
│   ├── day_2.py
│   └── test_day_2.py
├── 3/
│   ├── day_3.py
│   └── test_day_3.py
├── 4/
│   ├── day_4.py
│   └── test_day_4.py
├── CODING_GUIDELINES.md
├── create_day.py
└── pytest.ini
```

## Running Solutions

### Individual Days
```bash
cd X  # where X is the day number
python day_X.py
```

### Running Tests
```bash
# All tests
pytest

# Specific day
cd X
python -m pytest test_day_X.py -v
```

## Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd advent-of-code-2025
   ```

2. **Install dependencies**
   ```bash
   pip install pytest
   ```

3. **Add your puzzle input**
   - Create `input.txt` in each day's directory
   - Add your personal puzzle input from adventofcode.com

4. **Create new day**
   ```bash
   python create_day.py X  # where X is the day number
   ```

## Coding Guidelines

This project follows specific coding principles documented in [CODING_GUIDELINES.md](CODING_GUIDELINES.md):

1. **Correctness** > Readability > Minimal code > No premature optimization
2. Start with the **simplest possible approach**
3. Use **basic functions** over classes unless absolutely necessary
4. **Question every line** - "Is this really needed?"

## Progress

| Day | Part 1 | Part 2 | Notes |
|-----|--------|--------|--------|
| 1   | ⭐     | ⭐     | Dial simulation with zero crossings |
| 2   | ⭐     | ⭐     | Pattern matching with regex |
| 3   | ⭐     | ⭐     | Digit selection algorithms |
| 4   | ⭐     | ⭐     | 2D grid paper roll detection |

## Notes

- Input files (`input.txt`) are excluded from git for privacy
- Sample test files (`test.txt`) contain example data from puzzle descriptions
- All solutions include comprehensive test cases
- Code prioritizes clarity and simplicity over premature optimization