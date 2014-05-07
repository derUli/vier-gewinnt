red = gameObject.preloadImage(os.path.join(gameObject.image_dir, "red.png"))
blue = gameObject.preloadImage(os.path.join(gameObject.image_dir, "blue.png"))
nothing = gameObject.preloadImage(os.path.join(gameObject.image_dir, "nothing.png"))

padding_top = 20
padding_left = 80

posX = padding_left
posY = padding_top

for line in gameObject.game_vars["field"]:
    for row in line:
        posX += gameObject.game_vars["cell_size"][0]
        if row == 0:
            gameObject.image.blit(nothing, (posX, posY))
        elif row == 1:
            gameObject.image.blit(red, (posX, posY))
        elif row == 2:
            gameObject.image.blit(blue, (posX, posY))
            
    posX = padding_left
    posY += gameObject.game_vars["cell_size"][1]
