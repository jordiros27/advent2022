with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]

res = 0

for item in items:
    mitad = len(item) / 2
    str1 = item[:int(mitad)]
    str2 = item[int(mitad):]
    for letter in str1:
        if str.__contains__(str2, letter):
            if ord(letter) - ord('a') >= 0:
                res += ord(letter) - ord('a') + 1
                str2 = str2.replace(letter[-1], '')
            else:
                res += ord(letter[-1]) - ord('A') + 27
                str2 = str2.replace(letter[-1], '')

print(res)