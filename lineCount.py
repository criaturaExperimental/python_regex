text = open('chat.txt')
# here we read the whole text as a single string line
brute = text.read()
count = 0

for line in text:
    count = count + 1

print "there are", count, "lines in the text provided"

print len(brute), "total characters in the text"
