
with open('input') as f:
    s = f.read().strip().split('\n\n')

drawn = [int(i) for i in s[0].split(',')]

boards = [[[int(i) for i in line.split()] for line in board.split('\n')] for board in s[1:]]
boards_drawn = [[[False for i in range(5)] for i in range(5)] for board in s[1:]]

boards_won = []

def find_winning_board():
    for d in drawn:
        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                for k, num in enumerate(line):
                    if num == d:
                        boards_drawn[i][j][k] = True

        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                line_true = True
                for k, num in enumerate(line):
                    line_true = line_true and boards_drawn[i][j][k]
                if line_true:
                    if i not in boards_won:
                        boards_won.append(i)
                        if len(boards_won) == len(boards):
                            return i, d

            for k, column in enumerate(board):
                column_true = True
                for j, num in enumerate(column):
                    column_true = column_true and boards_drawn[i][j][k]
                if column_true:
                    if i not in boards_won:
                        boards_won.append(i)
                        if len(boards_won) == len(boards):
                            return i, d

i, d = find_winning_board()
winning_board = boards[i]
winning_board_drawn = boards_drawn[i]

s = 0
for j, line in enumerate(winning_board):
    for k, num in enumerate(line):
        if not winning_board_drawn[j][k]:
            s += num
print(s*d)