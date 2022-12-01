with open('calories.txt', 'r') as f:
    elfs = [line.strip() for line in f]

first, second, third, actualElf = 0, 0, 0, 0
for elf in elfs:
    if elf.isdigit():
        actualElf = actualElf + int(elf)
    else:
        if(first < actualElf):
            third = second
            second = first
            first = actualElf
        elif(second < actualElf):
            third = second
            second = actualElf
        elif(third <actualElf):
            third = actualElf
        actualElf = 0

print(first+second+third)