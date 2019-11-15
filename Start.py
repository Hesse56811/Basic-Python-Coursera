from operator import itemgetter
from math import *

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
presedents = dict()
Myset = set()
voice = 0
for i in inFile:
    participant = i.rstrip('\n')
    voice += 1
    if participant in presedents:
        presedents[participant] += 1
    else:
        presedents[participant] = 1
    Myset.add(participant)
wordlist = list()
for participant in Myset:
    wordlist.append((presedents[participant], participant))
wordlist.sort(key=itemgetter(1), reverse=False)
wordlist.sort(key=itemgetter(0), reverse=True)
for i in range(len(wordlist)):
    if wordlist[0][0] > voice // 2:
        print(wordlist[0][1], file=outFile)
        break
    else:
        print(wordlist[0][1], file=outFile)
        print(wordlist[1][1], file=outFile)
        break
