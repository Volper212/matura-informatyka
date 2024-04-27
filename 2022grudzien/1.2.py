scores = {
    'A': 0,
    'B': 0,
}
with open('mecz.txt') as file:
    line = file.readline().strip()
    for team in line:
        scores[team] += 1
        if (scores['A'] >= 1000 or scores['B'] >= 1000) and abs(scores['A'] - scores['B']) >= 3:
            print(f'{team} {scores["A"]}:{scores["B"]}')
            break
