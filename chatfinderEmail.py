import re

raw = open('chat.txt')

for line in raw:
    line = line.rstrip()
    # dot needs to be escaped
    if re.search('\S+@\S+\.', line):
        print line
