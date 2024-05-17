boards = []
with open("szachy.txt") as file:
    board = []
    for line in file.readlines():
        line = line.strip()
        if line == "":
            boards.append(board)
            board = []
        else:
            board.append(line)
    if len(board) != 0:
        boards.append(board)
white = 0
black = 0
for board in boards:
    check = False
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] == 'W':
                for c in range(col - 1, -1, -1):
                    if board[row][c] != '.':
                        if board[row][c] == 'k':
                            check = True
                        break
                for c in range(col + 1, 8):
                    if board[row][c] != '.':
                        if board[row][c] == 'k':
                            check = True
                        break
                for r in range(row - 1, -1, -1):
                    if board[r][col] != '.':
                        if board[r][col] == 'k':
                            check = True
                        break
                for r in range(row + 1, 8):
                    if board[r][col] != '.':
                        if board[r][col] == 'k':
                            check = True
                        break
    if check:
        white += 1
    check = False
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] == 'w':
                for c in range(col - 1, -1, -1):
                    if board[row][c] != '.':
                        if board[row][c] == 'K':
                            check = True
                        break
                for c in range(col + 1, 8):
                    if board[row][c] != '.':
                        if board[row][c] == 'K':
                            check = True
                        break
                for r in range(row - 1, -1, -1):
                    if board[r][col] != '.':
                        if board[r][col] == 'K':
                            check = True
                        break
                for r in range(row + 1, 8):
                    if board[r][col] != '.':
                        if board[r][col] == 'K':
                            check = True
                        break

    if check:
        black += 1
print(white, black)
