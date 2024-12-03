reports = []


def parse_levels(levels):
    level_sum = levels[0]-levels[1]
    direction = 0
    if level_sum > 0:
        direction = 1
    prev = levels[0]
    for level in levels[1:]:
        match direction:
            case 1:
                # print("Decreasing")
                if level > prev:
                    # print("Direction changed")
                    return False
                elif level - prev == 0 or prev - level > 3:
                    # print("Difference is 0 or too big")
                    # print(level, ", ", prev)
                    return False
            case 0:
                # print("Increasing")
                if level < prev:
                    # print("Direction changed")
                    return False
                elif prev - level == 0 or prev - level < -3:
                    # print("Difference is 0 or too big")
                    return False
        prev = level

    return True


def parse_reports(report):
    sum = 0
    for levels in report:
        if parse_levels(levels):
            sum += 1

    return sum


with open("input.txt", 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        reports.append(row)

print(parse_reports(reports))
