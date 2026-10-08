fhand = input ('Enter file name: ')
for line in fhand:
    line = line.rstrip()
    if line.startswith('mbox-short.txt ') : continue
    words = line.split()
    print(words)