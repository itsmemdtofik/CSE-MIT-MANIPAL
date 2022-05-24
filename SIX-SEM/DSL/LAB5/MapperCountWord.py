import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    words = line
    for word in words:
        print("%s\t%s" % (word, 1))
