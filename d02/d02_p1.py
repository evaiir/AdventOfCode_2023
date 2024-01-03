bag = open("inpt.txt").read()
games = bag.splitlines()
cube_limit = {"red": 12, "green": 13, "blue": 14}
total = 0

for game in games:
    possible = True
    game_num = int(game.split(" ")[1].rstrip(":"))
    cube_sets = game.split(":")[1].split(";")

    for cube_set in cube_sets:
        cube_groups = cube_set.split(",")

        for color in cube_groups:
            split_string = color.split(" ")
            cube_color = split_string[2]
            cube_quantity = int(split_string[1])

            if cube_color in cube_limit:
                limit = cube_limit[cube_color]
                if cube_quantity > limit:
                    possible = False

    if possible:
        total += game_num

print(total)
