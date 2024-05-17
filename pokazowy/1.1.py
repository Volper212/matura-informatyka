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
count = 0
largest = 0
for board in boards:
    isEmpty = [True] * 8
    for row in board:
        for i in range(len(row)):
            if row[i] != '.':
                isEmpty[i] = False
    if sum(isEmpty) > 0:
        count += 1
    largest = max(largest, sum(isEmpty))
print(count, largest)
