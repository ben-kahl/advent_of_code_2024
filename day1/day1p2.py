left_col = []
right_col = []
counts = []


def find_occurences(left, right):
    for elem in left:
        val = elem * right.count(elem)
        counts.append((elem, val))


def calc_similarity(left, right):
    find_occurences(left, right)
    sum = 0
    for _, val in counts:
        sum += val
    return sum


with open('input.txt', 'r') as file:
    for line in file:
        if line.strip():  # Check if the line is not empty
            left, right = map(int, line.split())
            left_col.append(left)
            right_col.append(right)


left_col.sort()
right_col.sort()
print(calc_similarity(left_col, right_col))
