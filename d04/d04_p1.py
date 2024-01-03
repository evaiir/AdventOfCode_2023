card_pile = open("inpt.txt").read();
cards = card_pile.splitlines();
score_total = 0;

for card in cards:
    win_count = 0
    card_score = 0;
    numbers = card.split(":")[1]
    winning_numbers = [num for num in numbers.split("|")[0].split(" ") if num]
    elf_numbers = [num for num in numbers.split("|")[1].split(" ") if num]
    print(winning_numbers)
    print(elf_numbers)
    for num in elf_numbers:
        if num in winning_numbers:
            win_count += 1

    print(win_count)

    if win_count > 0:
        card_score = 1
        for point in range(2, win_count+1):
            card_score *= 2

    score_total += card_score

print(score_total)
