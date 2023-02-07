def on_button_pressed_a():
    global directionx, directiony, direx, direy
    directionx = 0
    directiony = 1
    direx = directionx
    direy = directiony
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global direx, direy, directionx, directiony
    direx = directionx
    direy = directiony
    directionx = -1
    directiony = 0
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    global direx, direy, directionx, directiony
    direx = directionx
    direy = directiony
    directionx = 0
    directiony = -1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    global direx, direy, directionx, directiony
    direx = directionx
    direy = directiony
    directionx = 1
    directiony = 0
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def rapple():
    ok = 0
    while ok == 0:
        n = 0
        for n in range(0, RINGS.length-1):
            apple.set(LedSpriteProperty.X, randint(0, 4))
            apple.set(LedSpriteProperty.Y, randint(0, 4))
            if not apple.is_touching(RINGS[n]):
                ok = 1
direy = 0
direx = 1
directiony = 0
directionx = 1
game.set_score(0)
RINGS = [game.create_sprite(1, 2), game.create_sprite(0, 2)]
apple = game.create_sprite(2, 2)
rapple()

def on_forever():
    global directionx, directiony
    basic.pause(1000)
    RINGS.unshift(game.create_sprite(RINGS[0].get(LedSpriteProperty.X) + directionx,
            RINGS[0].get(LedSpriteProperty.Y) + directiony))
    if RINGS[0].is_touching_edge():
        game.game_over()
    if RINGS[0].is_touching(apple):
        rapple()
        game.add_score(1)
    else:
        RINGS[len(RINGS) - 1].delete()
        RINGS.remove_at(len(RINGS) - 1)
basic.forever(on_forever)
