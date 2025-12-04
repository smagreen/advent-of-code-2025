# pylint: disable=missing-module-docstring,missing-function-docstring

def read_input(filename):
    return [line.strip() for line in open(filename, 'r', encoding='utf-8')]

def part_1(data):
    """Solve part 1 of the puzzle"""
    total_sum = 0
    
    for bank in data:
        digits = [int(digit) for digit in str(bank) if digit.isdigit()]
        
        if len(digits) >= 2:
            # Step 1: Find the highest digit that's NOT the last digit
            max_value = -1
            max_index = -1
            for i in range(len(digits) - 1):  # Exclude last digit
                if digits[i] > max_value:
                    max_value = digits[i]
                    max_index = i
            
            # Step 2: Find the highest digit that follows the first digit
            second_max_value = -1
            for i in range(max_index + 1, len(digits)):
                if digits[i] > second_max_value:
                    second_max_value = digits[i]
            
            # Concatenate the two digits
            concatenated = int(str(max_value) + str(second_max_value))
            total_sum += concatenated
    
    return total_sum

def part_2(data):
    """Optimized version of part 2 - assumes sufficient digits are always available"""
    total_sum = 0
    
    for bank in data:
        digits = [int(digit) for digit in str(bank) if digit.isdigit()]
        
        # Create the largest possible 12-digit number maintaining order
        largest_number = ""
        last_used_index = -1
        
        # Build the 12-digit number digit by digit
        for position in range(12):
            best_digit = -1
            best_index = -1
            
            # Only consider digits after the last used index (maintain order)
            start_index = last_used_index + 1
            
            # Since we know there are always enough digits, we can be more aggressive
            # Find the highest digit that still leaves enough remaining positions
            min_required_remaining = 11 - position  # positions still needed after this one
            
            for i in range(start_index, len(digits) - min_required_remaining):
                if digits[i] > best_digit:
                    best_digit = digits[i]
                    best_index = i
            
            largest_number += str(best_digit)
            last_used_index = best_index
        
        total_sum += int(largest_number)
    
    return total_sum

def main():
    """Main function to run the solution"""
    input_data = read_input('./3/input.txt')
    print(f"Part 1 = {part_1(input_data)}")
    print(f"Part 2 = {part_2(input_data)}")

if __name__ == "__main__":
    main()
