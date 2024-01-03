almanac = open("inpt.txt").read().split("\n\n")

seeds = [int(seed) for seed in almanac[0].split(": ")[1].split()]
almanac.pop(0)

mapping = [part.splitlines()[1:] for part in almanac]

j = 0
while j < len(seeds):
    for translations in mapping:
        value_changed = False
        i = 0
        while i < len(translations) and not value_changed:
            dest, src, rng = [int(x) for x in translations[i].split()]
            if src <= seeds[j] < src + rng:
                seeds[j] = dest + seeds[j] - src
                value_changed = True

            i += 1
    j += 1

print(min(seeds))
