name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    sender = words[1]
    counts[sender] = counts.get(sender,0) + 1

bigcount = None
bigsender = None
for sender,count in counts.items():
    if bigcount is None or count > bigcount:
        bigsender = sender
        bigcount = count

print(bigsender, bigcount)
