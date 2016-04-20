import re

raw = open('chat.txt')

main = []

for line in raw:
    line = line.rstrip()

    res = re.findall('\S+@\S+\.\S+', line)
    # adds links with google maps @ position so it needs to be filtered
    if len(res) > 0:
        if not re.search('/', res[0]):
            res2 = re.findall('@([^ ]*)', res[0])
            main.extend(res2)

print main
