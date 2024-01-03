card_pile = open("inpt.txt").read();
cards = card_pile.splitlines();
card_num = [1] * len(cards)

for i in range(len(cards)):
    win_count = 0
    card_score = 0;
    numbers = cards[i].split(":")[1]
    winning_numbers = [num for num in numbers.split("|")[0].split(" ") if num]
    elf_numbers = [num for num in numbers.split("|")[1].split(" ") if num]
    for num in elf_numbers:
        if num in winning_numbers:
            win_count += 1
            card_num[i + win_count] += card_num[i]

print(sum(card_num))
