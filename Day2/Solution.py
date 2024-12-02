def is_safe(report):
    """
    Determines if a report is safe.
    A report is safe if:
    1. All levels are either increasing or decreasing.
    2. The difference between any two adjacent levels is at least 1 and at most 3.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are either positive or negative (strictly increasing or decreasing)
    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return all_increasing or all_decreasing

def count_safe_reports(filename):
    """
    Reads reports from the input file and counts how many are safe.
    """
    safe_count = 0
    with open(filename, "r") as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe(report):
                safe_count += 1
    return safe_count

# Specify the input file
input_file = "input.txt"

# Calculate the number of safe reports
safe_reports = count_safe_reports(input_file)
print(f"Number of safe reports: {safe_reports}")
