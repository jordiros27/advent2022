with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]

res = 0

def get_score(char):
    # I put the problem in ChatGPT and it gave the same code as this HAHAHAHA I don't like where this is going
    if char.islower():
        return ord(char) - ord("a") + 1
    else:
        return ord(char) - ord("A") + 27

for ind in range(0, len(items), 3):
    res += get_score(
        min(
            set(items[ind]) &
            set(items[ind + 1]) &
            set(items[ind + 2]))
    )

print(res)