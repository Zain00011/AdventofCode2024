def parse_input(file_path):
    """Parses the input file to extract ordering rules and updates."""
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
    
    # Split the input into rules and updates
    split_index = lines.index("")  # Find the blank line separating the two sections
    rules = lines[:split_index]
    updates = lines[split_index + 1:]
    
    # Process rules into tuples
    rules = [tuple(map(int, rule.split("|"))) for rule in rules]
    
    # Process updates into lists of integers
    updates = [list(map(int, update.split(","))) for update in updates]
    
    return rules, updates


def is_update_correct(update, rules):
    """Checks if the given update respects all applicable ordering rules."""
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):  # Rule violated
                return False
    return True


def correct_order(update, rules):
    """
    Reorders the pages in the update according to the rules.
    Implements a topological sort based on the rules.
    """
    # Build a graph and in-degree count
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages = set(update)

    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Perform topological sort
    queue = deque([page for page in pages if in_degree[page] == 0])
    ordered_pages = []

    while queue:
        current = queue.popleft()
        ordered_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_pages


def find_middle_number(update):
    """Finds the middle page number in the update."""
    middle_index = len(update) // 2
    return update[middle_index]


def main():
    # Parse the input
    rules, updates = parse_input("input.txt")
    
    middle_sum = 0  # To accumulate the sum of middle page numbers of corrected updates
    
    for update in updates:
        if not is_update_correct(update, rules):
            corrected_update = correct_order(update, rules)
            middle_sum += find_middle_number(corrected_update)
    
    print(f"Sum of middle page numbers after correcting updates: {middle_sum}")


if __name__ == "__main__":
    main()
