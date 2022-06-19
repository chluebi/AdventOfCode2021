def main():
    with open('input') as f:
        s = f.read().strip().split('\n\n')

games = {(6, 0, 10, 0, 0): 1}

def mod(x):
    y = x
    while y > 10:
        y -= 10
    return y

p1_total = 0
p2_total = 0

while True:
    game_sum = 0
    score_sum = 0
    lowest_score = 100
    for (p1_pos, p1_score, p2_pos, p2_score, turn), value in games.items():
        game_sum += value
        score_sum += value*(p1_score + p2_score)/2
        lowest_score = min(p1_score, p2_score, lowest_score)
    print(game_sum)
    print(score_sum/game_sum)
    print('lowest score', lowest_score)

    new_games = {}
    for (p1_pos, p1_score, p2_pos, p2_score, turn), n in games.items():
        if turn == 0:
            for roll1 in range(1, 4):
                for roll2 in range(1, 4):
                    for roll3 in range(1, 4):
                        total = roll1 + roll2 + roll3
                        key = (mod(p1_pos + total), p1_score + mod(p1_pos + total), p2_pos, p2_score, 1)

                        if key in new_games:
                            new_games[key] += n 
                        else:
                            new_games[key] = n
        else:
            for roll1 in range(1, 4):
                for roll2 in range(1, 4):
                    for roll3 in range(1, 4):
                        total = roll1 + roll2 + roll3
                        key = (p1_pos, p1_score, mod(p2_pos + total), p2_score + mod(p2_pos + total), 0)

                        if key in new_games:
                            new_games[key] += n 
                        else:
                            new_games[key] = n

    games = {}

    for (p1_pos, p1_score, p2_pos, p2_score, turn), n in new_games.items():
        if p1_score >= 21:
            p1_total += n
        elif p2_score >= 21:
            p2_total += n
        else:
            key = (p1_pos, p1_score, p2_pos, p2_score, turn)

            if key in games:
                games[key] += n 
            else:
                games[key] = n
    
    if len(games) == 0:
        break

print(p1_total, p2_total)
print('TOTAL', max(p1_total, p2_total))