with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]

sum = 0
for item in items:
    x = item.split(',')
    str1 = x[0].split('-')
    str2 = x[1].split('-')

    if int(str2[0]) <= int(str1[0]) and int(str2[-1]) <= int(str1[-1]) and int(str2[-1]) >= int(str1[0]):
        sum += 1
    elif int(str2[0]) >= int(str1[0]) and int(str2[-1]) >= int(str1[-1]) and int(str2[0]) <= int(str1[-1]):
        sum += 1
    elif int(str2[0]) >= int(str1[0]) and int(str2[-1]) <= int(str1[-1]):
        sum += 1
    elif int(str2[0]) <= int(str1[0]) and int(str2[-1]) >= int(str1[-1]):
        sum += 1

print(sum)