bag = open("inpt.txt").read()
games = bag.splitlines()
total = 0

for game in games:
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    game_num = int(game.split(" ")[1].rstrip(":"))
    cube_sets = game.split(":")[1].split(";")

    for cube_set in cube_sets:
        cube_groups = cube_set.split(",")

        for color in cube_groups:
            split_string = color.split(" ")
            cube_color = split_string[2]
            cube_quantity = int(split_string[1])

            if cube_color in min_cubes:
                if cube_quantity > min_cubes[cube_color]:
                    min_cubes[cube_color] = cube_quantity

    cube_power = 1
    for color in min_cubes:
        cube_power *= min_cubes[color]

    total += cube_power

print(total)
