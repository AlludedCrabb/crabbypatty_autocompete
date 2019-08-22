import fileinput

instructions = list(fileinput.input())
numplayers = int(instructions[0])
board = instructions[1][6:].split()
num_spaces = len(board)
cards = instructions[2][6:].split()
pos = [0] * numplayers
card = 0
nowinner = True
while nowinner:
    for i, p in enumerate(pos):
        curr_card = cards[card]
        pos[i] += cards[p+1:].index(curr_card) + 1
        print(f"Player {i+1} moves to {curr_card}")
        if pos[i] == num_spaces -1:
            nowinner = False
            print(f"Player {i+1} wins!")
        card += 1
