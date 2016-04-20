import re

raw = open('chat.txt')

for line in raw:
    line = line.rstrip()
    if re.search('Marino.*:', line):
        print line
