gameObject.game_vars["board_width"] = 7
gameObject.game_vars["board_height"] = 6
gameObject.game_vars["cell_size"] = (70,70)


gameObject.game_vars["field"] = []

for i in range(gameObject.game_vars["board_height"]):
    line = []
    for i in range(gameObject.game_vars["board_width"]):
        line.append(0)
    gameObject.game_vars["field"].append(line)
