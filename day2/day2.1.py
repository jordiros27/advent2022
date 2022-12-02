with open('input.txt', 'r') as f:
    plays = [line.strip() for line in f]

opponent = ["A", "B", "C"]
you = ["X", "Y", "Z"]

sum = 0
for play in plays:
    o, y = play.split()
    o = opponent.index(o)
    y = you.index(y)
    if y == 0:
        sum += (o - 1) % 3 + 1
    if y == 1:
        sum += o + 4
    if y == 2:
        sum += (o + 1) % 3 + 1 + 6
 

print(sum)