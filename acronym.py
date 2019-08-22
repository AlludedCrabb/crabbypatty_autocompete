import fileinput
acronym = ""
for line in fileinput.input():
    a = line.split(' ')
    for w in a:
        if w[0].isupper():
            acronym += w[0]
print(acronym)
