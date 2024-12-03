import re

def sum_valid_multiplications(input_file):
    # Read the corrupted memory from the input file
    with open(input_file, "r") as file:
        data = file.read()
    
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    
    # Find all matches
    matches = re.findall(pattern, data)
    
    # Calculate the sum of all valid multiplications
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

# Example usage
input_file = "input.txt"
result = sum_valid_multiplications(input_file)
print("The sum of all valid multiplications is:", result)
