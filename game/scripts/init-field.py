gameObject.game_vars["board_width"] = 7
gameObject.game_vars["board_height"] = 6
gameObject.game_vars["cell_size"] = (70,70)


gameObject.game_vars["field"] = []

for i in range(gameObject.game_vars["board_height"]):
    line = []
    for i in range(gameObject.game_vars["board_width"]):
        line.append(0)
    gameObject.game_vars["field"].append(line)


gameObject.game_vars["field"][0][0] = 1

gameObject.game_vars["field"][3][4] = 1
