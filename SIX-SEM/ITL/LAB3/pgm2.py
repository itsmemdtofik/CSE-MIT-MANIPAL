f = open("input.txt", "r")
s = f.read()
f.close()
f = open("input.txt", "w+")
s = s[::-1]
f.write(s)
f.close()
