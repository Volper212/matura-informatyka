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
smallest = 1000000
for board in boards:
    pieces = {'K': 0, 'W': 0, 'S': 0, 'H': 0, 'G': 0, 'P': 0, 'k': 0, 'w': 0, 's': 0, 'h': 0, 'g': 0, 'p': 0}
    for row in board:
        for char in row:
            if char != '.':
                pieces[char] += 1
    for piece, c in pieces.items():
        if piece.islower() and c != pieces[piece.upper()]:
            break
    else:
        count += 1
        smallest = min(smallest, sum(pieces.values()))
print(count, smallest)
