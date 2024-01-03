paper = open("inpt.txt").read().splitlines()
times = paper[0].split(":")[1].split()
times = [time for time in times if time.isnumeric()]
total_time = int("".join(times))
top_distance = paper[1].split(":")[1].split()
top_distance = [distance for distance in top_distance if distance.isnumeric()]
distance_to_beat = int("".join(top_distance))

possibles_wins = 0
for j in range(total_time):
    speed = j
    travel_time = total_time - j
    travel_dist = travel_time * speed
    if travel_dist > distance_to_beat:
        possibles_wins += 1

print(possibles_wins)
