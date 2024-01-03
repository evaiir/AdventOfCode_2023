directions, *instructions = open("inpt.txt").read().splitlines()
instructions.pop(0)
directions = [1 if char == "R" else 0 for char in directions]

map_map = {}
curr_pos = "AAA"
#for line in instructions:
for line in instructions:
    map_map[line[0:3]] = (line[7:10], line[12:15])

step_count = 0
while curr_pos != "ZZZ":
    command = directions[step_count % len(directions)]
    curr_pos = map_map[curr_pos][command]
    step_count += 1

print(step_count)
