paper = open("inpt.txt").read().splitlines()
times = paper[0].split(":")[1].split()
times = [int(time) for time in times if time.isnumeric()]
top_distance = paper[1].split(":")[1].split()
top_distance = [int(distance) for distance in top_distance if distance.isnumeric()]

possibles_outcomes = 1
for i in range(len(times)):
    distance_to_beat = top_distance[i]
    total_time = times[i]
    possibles_wins = 0
    for j in range(total_time):
        speed = j
        travel_time = total_time - j
        travel_dist = travel_time * speed
        if travel_dist > distance_to_beat:
            possibles_wins += 1

    possibles_outcomes *= possibles_wins

print(possibles_outcomes)
