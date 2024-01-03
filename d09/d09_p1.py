def find_value(line):
    if line[0] == 0 and line[-1] == 0:
        return line[-1]

    diff_sequence = [b - a for a, b in zip(line, line[1:])]
    return line[-1] + find_value(diff_sequence)


report = open("inpt.txt").read().splitlines()

extrapolated_sum = sum(find_value([int(x) for x in line.split()]) for line in report)

print(extrapolated_sum)
