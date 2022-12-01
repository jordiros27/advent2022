with open('calories.txt', 'r') as f:
    elfs = [line.strip() for line in f]

maxElf, actualElf = 0, 0
for elf in elfs:
    if elf.isdigit():
        actualElf = actualElf + int(elf)
    else:
        if(maxElf < actualElf):
            maxElf=actualElf
        actualElf = 0

print(maxElf)