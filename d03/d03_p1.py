def get_neighbors(coord):
    i, j = coord
    rows, cols = len(schema), len(schema[0])

    neighbors = [
        (x, y)
        for x in range(i - 1, i + 2)
        for y in range(j - 1, j + 2)
        if 0 <= x < rows and 0 <= y < cols and (x != i or y != j)
    ]

    return neighbors


def find_number(coord):
    i, j = coord

    if not schema[i][j].isnumeric():
        return -1

    number = ""
    while j >= 0 and schema[i][j].isnumeric():
        number = schema[i][j] + number
        j -= 1

    j = coord[1] + 1
    while j < len(schema[i]) and schema[i][j].isnumeric():
        number = number + schema[i][j]
        j += 1

    return int(number) if number.isnumeric() else -1


schema = open("inpt.txt").read().splitlines()

symbols = [
    (i, j)
    for i in range(len(schema))
    for j in range(len(schema[0]))
    if schema[i][j] not in "0123456789."
]

part_number_map = {
    coord: list(
        set(
            num
            for neighbor in get_neighbors(coord)
            if (num := find_number(neighbor)) > 0
        )
    )
    for coord in symbols
}

part_sum = sum(sum(nums) for nums in part_number_map.values())
print(part_sum)
