game = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def game_board(game_map=game, player=0, row=0, column=0, just_display=False):
    print("  0  1  2")
    if not just_display:
        game_map[row][column] = player
    for count, row in enumerate(game_map):
        print(count, row)
    return game_map

game_board(game, 1,2,1)
print(game_board)
