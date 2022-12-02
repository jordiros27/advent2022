with open('input.txt', 'r') as f:
    plays = [line.strip() for line in f]

opponent = ["A", "B", "C"]
you = ["X", "Y", "Z"]

sum, aux = 0, 0
for play in plays:
    o, y = play.split()
    o = opponent.index(o)
    y = you.index(y)
    sum += y + 1
    aux = (y - o) % 3
    if aux == 1:
        sum += 6
    elif aux == 0:
        sum += 3

print(sum)