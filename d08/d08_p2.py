import math

def find_single_solution(position):
    step_count = 0
    while position[-1] != "Z":
        command = directions[step_count % len(directions)]
        position = map_map[position][command]
        step_count += 1
    return step_count


directions, *instructions = open("inpt.txt").read().splitlines()
instructions.pop(0)
directions = [1 if char == "R" else 0 for char in directions]

map_map = {}
# for line in instructions:
curr_pos = []
for line in instructions:
    map_map[line[0:3]] = (line[7:10], line[12:15])
    if line[2] == "A":
        curr_pos.append(line[0:3])

loop_steps = []
for pos in curr_pos:
    loop_steps.append(find_single_solution(pos))

step_count = math.lcm(*loop_steps)

print(step_count)
