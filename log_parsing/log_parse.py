file = open("log.txt")
pout = open("perr.txt", mode="w")
mout = open("merr.txt", mode="w")

for line in file:
    if line[0:2] != 'Do':
        if line[0] == 'M':
            mout.write(line)
        elif line[0] == 'P':
            pout.write(line)
            #  print(line.split(": ")[1].rstrip().split(".")[0] + ".jpg", end=' ')