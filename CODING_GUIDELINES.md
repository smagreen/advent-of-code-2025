# Advent of Code 2025 - Coding Guidelines

## Priority Order for All Solutions:
1. **Correctness** - Solution must work
2. **Readability** - Code should be immediately understandable
3. **Minimal code** - Fewest lines that still maintain clarity
4. **No premature optimization** - Don't optimize until it works

## Implementation Rules:
- Start with the **simplest possible approach**
- Use **basic functions** over classes unless absolutely necessary
- Avoid **unnecessary abstractions** or design patterns
- **Question every line** - "Is this really needed?"
- **Direct path to solution** - map logic directly to problem description
- Eliminate **duplicate code** and redundant operations

## Red Flags to Avoid:
- Classes when functions would suffice
- Passing the same parameters repeatedly
- Multiple functions doing similar things
- Complex inheritance or abstractions
- More than ~50 lines for simple problems

## Good Patterns:
- Single responsibility functions
- List comprehensions where appropriate
- Direct set/dict operations
- Minimal parameter passing
- Clear variable names

## Example Structure:
```python
def read_input(filename):
    # Simple file reading

def solve_part_1(data):
    # Direct solution approach

def solve_part_2(data):
    # Build on part_1 or use shared utilities

def main():
    # Simple execution
```

Remember: **Simple and correct beats complex and clever**