document = open("inpt.txt").read().splitlines()

calibration_sum = 0
for line in document:
    for char in line:
        if char.isdigit():
            calibration_sum += 10*int(char)
            break

    for char in reversed(line):
        if char.isdigit():
            calibration_sum += int(char)
            break

print(calibration_sum)
