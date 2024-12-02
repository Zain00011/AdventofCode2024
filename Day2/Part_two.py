def is_safe(report):
    """
    Determines if a report is safe without any modifications.
    A report is safe if:
    1. All levels are either increasing or decreasing.
    2. The difference between any two adjacent levels is at least 1 and at most 3.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are either positive or negative (strictly increasing or decreasing)
    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return all_increasing or all_decreasing

def is_safe_with_dampener(report):
    """
    Determines if a report is safe with the Problem Dampener.
    This allows removing a single bad level to make the report safe.
    """
    # If the report is already safe, return True
    if is_safe(report):
        return True
    
    # Try removing each level and check if the remaining report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    
    # If no single removal makes it safe, return False
    return False

def count_safe_reports_with_dampener(filename):
    """
    Reads reports from the input file and counts how many are safe,
    considering the Problem Dampener.
    """
    safe_count = 0
    with open(filename, "r") as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe_with_dampener(report):
                safe_count += 1
    return safe_count

# Specify the input file
input_file = "input.txt"

# Calculate the number of safe reports with the Problem Dampener
safe_reports_with_dampener = count_safe_reports_with_dampener(input_file)
print(f"Number of safe reports with the Problem Dampener: {safe_reports_with_dampener}")
