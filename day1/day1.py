import heapq

pairs = []
left_column = []
right_column = []


def create_pairs(left, right):
    heapq.heapify(left)
    heapq.heapify(right)
    while left:
        min_left = heapq.heappop(left)
        min_right = heapq.heappop(right)
        pairs.append((min_left, min_right))


def calc_distance(left, right):
    create_pairs(left, right)
    sum = 0
    for pair in pairs:
        distance = pair[0] - pair[1]
        sum += abs(distance)

    return sum


with open('input.txt', 'r') as file:
    for line in file:
        if line.strip():  # Check if the line is not empty
            left, right = map(int, line.split())
            left_column.append(left)
            right_column.append(right)

print(calc_distance(left_column, right_column))
