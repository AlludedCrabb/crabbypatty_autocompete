from fileinput import input

everything = list(input())

suspects = everything[0][9:].strip().split(',')
weapons = everything[1][8:].strip().split(',')
rooms = everything[2][6:].strip().split(',')
# print( suspects, weapons, rooms)
# clues = everything
for line in everything[4:]:
    clue = line.strip().split(' ')
    # print("clue is " + " ".join(clue))
    if clue[1] != 'the':
        # print(" ".join(clue[1:]) in suspects) 
        suspects.remove(" ".join(clue[1:]))
        # print(suspects)
    else:
        thing = " ".join(clue[2:])
        if thing in weapons:
            weapons.remove(thing)
        else:
            rooms.remove(thing)
print(suspects[0])
print("in the " + rooms[0])
print("with the " + weapons[0])