import argparse
import itertools

# Create parser for command-line options using argparse

parser = argparse.ArgumentParser(description = "Complete Saturation Mutagenesis for miRNAs")
parser.add_argument("mirna", type = str, metavar = " ", help = "Enter miRNA name")
parser.add_argument("sequence", type = str, metavar = " ", help = "Enter miRNA sequence")
parser.add_argument("start", type = int, metavar = " ", help = "miRNA sequence length")


args = parser.parse_args()

mirna = args.mirna
sequence = args.sequence.upper()
start = args.start

y = 0

l = []

while y < len(sequence):
    s = list(sequence)
    if s[y] != 'A':
        s[y] = 'A'
        l.append(s[:])
    if s[y] != 'C':
        s[y] = 'C'
        l.append(s[:])
    if s[y] != 'G':
        s[y] = 'G'
        l.append(s[:])
    if s[y] != 'U':
        s[y] = 'U'
        l.append(s[:])
    if s[y] != 'T':
        s[y] = 'T'
        l.append(s[:])
    y = y + 1

# Get rid of duplicate lists within list

li = list(l for l,_ in itertools.groupby(l))


# Save to fasta file

x = 0
s = list(sequence)

filename = "%s.fasta" % mirna
f = open(filename, "a")
f.write(">" + mirna + " | wild-type" + "\n")
print(''.join(s), file = f)
f.close()

while x < len(li):
    f = open(filename, "a")
    s = list(sequence)
    if s != li[x]:
        out = [index for index, elem in enumerate(li[x])
                           if elem != s[index]] #gets unmatched list index
        diff = int("".join(list(map(str,out)))) #change index list to int
        strt = start + diff
        f.write(">" + mirna + " |" + " n." + str(strt) + str(s[diff]) + " > " + str(li[x][diff]) + "\n")
        print(''.join(li[x]), file = f)
    x += 1
    f.close()