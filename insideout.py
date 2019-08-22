import fileinput
for line in fileinput.input():
    line = line.strip()
    n = len(line)
    iseven = n%2 == 0
    if n == 1:
        result = line + line
    elif iseven:
        firsthalf = line[0:n//2]
        secondhalf = line[n//2:]
        result = firsthalf[::-1] + secondhalf[::-1]
    else:
        firsthalf = line[0:n//2+1]
        secondhalf = line[n//2:]
        result = firsthalf[::-1] + secondhalf[::-1]
    print(result)