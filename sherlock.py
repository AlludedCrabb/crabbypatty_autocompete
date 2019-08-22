from collections import Counter

import fileinput
for line in fileinput.input():
    wc = Counter(line)
    counts = list(wc.values())
    if max(counts) == min(counts):
        print('true')
    elif max(counts) == min(counts) + 1 and counts.count(max(counts)) == 1:
        print('true')
    else:
        print('false')

        