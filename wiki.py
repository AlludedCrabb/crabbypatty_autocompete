import input from fileinput

suspects = input()[9:].split(',')
weapons = input()[8:].split(',')
rooms = input()[6:].split(',')

clues = input()
for line in input():
    clue = line.split(' ')
    if clue[1] != 'the':
        suspects.remove(" ".join(clue[1:]))
    else:
        thing = " ".join(clue[2:])
        if thing in weapons:
            weapons.remove(thing)
        else:
            rooms.remove(thing)
    print(suspects[0])
    print("in the " + rooms[0])
    print("with the " + weapons[0])