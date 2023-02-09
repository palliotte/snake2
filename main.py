def rapple():
    global n
    ok = 0
    apple.set(LedSpriteProperty.X, randint(0, 4))
    apple.set(LedSpriteProperty.Y, randint(0, 4))
    while ok == 0:
        n = 0
        index = 0
        while index <= len(RINGS) - 1:
            if RINGS[n].is_touching(apple):
                apple.set(LedSpriteProperty.X, randint(0, 4))
                apple.set(LedSpriteProperty.Y, randint(0, 4))
            else:
                pass
            index += 1

def on_button_pressed_a():
    global directionx, directiony
    if not (directionx == 0) and not (directiony == -1):
        directionx = 0
        directiony = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global directionx, directiony
    if not (directionx == 1) and not (directiony == 0):
        directionx = -1
        directiony = 0
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    global directionx, directiony
    if not (directionx == 0) and not (directiony == 1):
        directionx = 0
        directiony = -1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    global directionx, directiony
    if not (directionx == -1) and not (directiony == 0):
        directionx = 1
        directiony = 0
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

n = 0
apple: game.LedSprite = None
RINGS: List[game.LedSprite] = []
directionx = 1
directiony = 0
game.set_score(0)
RINGS = [game.create_sprite(1, 2), game.create_sprite(0, 2)]
apple = game.create_sprite(2, 2)
rapple()

def on_forever():
    basic.pause(1000)
    RINGS.unshift(game.create_sprite(RINGS[0].get(LedSpriteProperty.X) + directionx,RINGS[0].get(LedSpriteProperty.Y) + directiony))
    if RINGS[0].is_touching_edge():
        if RINGS[0].get(LedSpriteProperty.X)==0 and directionx == -1 or RINGS[0].get(LedSpriteProperty.X)==4 and directionx == 1 or RINGS[0].get(LedSpriteProperty.Y)==0 and directiony == -1 or RINGS[0].get(LedSpriteProperty.Y)==4 and directionx == 1:
            game.game_over()
    if RINGS[0].is_touching(apple):
        rapple()
        game.add_score(1)
    else:
        RINGS[len(RINGS) - 1].delete()
        RINGS.remove_at(len(RINGS) - 1)
basic.forever(on_forever)
