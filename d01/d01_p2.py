translation = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

document = open("example.txt").read()

for word, num in translation.items():
    document = document.replace(word, num)
for word, num in translation.items():
    document = document.replace(word, num)

print(document)

calibration_sum = 0
for line in document.splitlines():
    for char in line:
        if char.isdigit():
            calibration_sum += 10*int(char)
            break

    for char in reversed(line):
        if char.isdigit():
            calibration_sum += int(char)
            break

print(calibration_sum)
