map = [list(line) for line in open("inpt.txt").read().splitlines()]

start = None
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "S":
            start = (i, j)

count = 0
pipe_face_down = ["S", "F", "7", "|"]
pipe_face_left = ["S", "J", "7", "-"]
pipe_face_up = ["S", "J", "L", "|"]
pipe_face_right = ["S", "L", "F", "-"]


def get_tunnel_path(i, j, count):
    last_visited = (i, j)
    if map[i - 1][j] in pipe_face_down:
        count += 1
        i -= 1
    elif map[i][j + 1] in pipe_face_left:
        count += 1
        j += 1
    elif map[i + 1][j] in pipe_face_up:
        count += 1
        i += 1
    elif map[i][j - 1] in pipe_face_right:
        count += 1
        j -= 1

    while map[i][j] != "S":
        if map[i][j] == "F":
            if map[i][j + 1] in pipe_face_left and (i, j + 1) != last_visited:
                map[i][j] = count
                count += 1
                j += 1
            elif map[i + 1][j] in pipe_face_up:
                map[i][j] = count
                count += 1
                i += 1

        elif map[i][j] == "7":
            if map[i + 1][j] in pipe_face_up and (i + 1, j) != last_visited:
                map[i][j] = count
                count += 1
                i += 1
            elif map[i][j - 1] in pipe_face_right:
                map[i][j] = count
                count += 1
                j -= 1

        elif map[i][j] == "J":
            if map[i - 1][j] in pipe_face_down and (i - 1, j) != last_visited:
                map[i][j] = count
                count += 1
                i -= 1
            elif map[i][j - 1] in pipe_face_right:
                map[i][j] = count
                count += 1
                j -= 1

        elif map[i][j] == "L":
            if map[i][j + 1] in pipe_face_left and (i, j + 1) != last_visited:
                map[i][j] = count
                count += 1
                j += 1
            elif map[i - 1][j] in pipe_face_down:
                map[i][j] = count
                count += 1
                i -= 1

        elif map[i][j] == "|":
            if map[i - 1][j] in pipe_face_down and (i - 1, j) != last_visited:
                map[i][j] = count
                count += 1
                i -= 1
            elif map[i + 1][j] in pipe_face_up:
                map[i][j] = count
                count += 1
                i += 1

        elif map[i][j] == "-":
            if map[i][j + 1] in pipe_face_left and (i, j + 1) is not last_visited:
                map[i][j] = count
                count += 1
                j += 1
            elif map[i][j - 1] in pipe_face_right:
                map[i][j] = count
                count += 1
                j -= 1

        last_visited = (i, j)

    return count


if start is not None:
    print(get_tunnel_path(*start, 0) // 2)
