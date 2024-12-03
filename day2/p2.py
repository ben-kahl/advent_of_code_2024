reports = []


def is_safe(levels):
    direction = levels[0] - levels[1]
    if direction > 0:
        direction = 1  # Decreasing
    else:
        direction = 0  # Increasing

    prev = levels[0]
    for level in levels[1:]:
        if direction == 1 and level > prev:  # Decreasing but found an increase
            return False
        elif direction == 0 and level < prev:  # Increasing but found a decrease
            return False
        elif abs(level - prev) > 3 or abs(level - prev) == 0:  # Invalid difference
            return False
        prev = level
    return True


def parse_levels(levels):
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        modified = levels[:i] + levels[i + 1:]
        if is_safe(modified):
            return True
    return False


with open("input.txt", 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        reports.append(row)

test = [[7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]]

print(sum(parse_levels(report) for report in reports))
