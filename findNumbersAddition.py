import re

raw = open('main.txt')

total = 0
main = []

for line in raw:
    line = line.rstrip()

    res = re.findall('[0-9]+', line)
    main.extend(res)

for number in main:
    total = total + int(number)

print total
