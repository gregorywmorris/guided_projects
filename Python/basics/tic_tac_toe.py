"""Python Tutorial"""
game = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    """Tic tac toe game"""
    try:
        print("  0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, rows in enumerate(game_map):
            print(count, rows)
        return game_map
    except IndexError as e:
        print("ERROR: make sure you input row/column as 0, 1, or 2.", e)


game_board(game, 1,2,1)
print(game_board)
