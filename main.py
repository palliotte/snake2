
def on_button_pressed_a():
    global directionx, directiony
    directionx = 0
    directiony = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global directionx, directiony
    directionx = -1
    directiony = 0
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_b():
    global directionx, directiony
    directionx = 0
    directiony = -1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    global directionx, directiony
    directionx = 1
    directiony = 0
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def apple():
    ok = 0
    while ok ==0:
        index = 0
        for index in range(len.RINGS-1):
            if apple.is_touching(RINGS[index]):
                apple.set(LedSpriteProperty.X, randint(0, 4))
                apple.set(LedSpriteProperty.Y, randint(0, 4))
            else:
                ok=1


directiony = 0
directionx = 0
RINGS: List[game.LedSprite] = []
game.set_score(0)
RINGS = [game.create_sprite(1, 2),game.create_sprite(0, 2)]
directionx = 1
directiony = 1
apple = game.create_sprite(2, 2)
apple()

def on_forever():
    basic.pause(1000)
    RINGS.unshift(game.create_sprite(RINGS[0].get(LedSpriteProperty.X) + directionx,
            RINGS[0].get(LedSpriteProperty.Y) + directiony))
    if RINGS[0].is_touching(apple):
        apple()
        game.add_score(1)
    else:    
        RINGS[RINGS.length-1].delete()
        RINGS.pop()
basic.forever(on_forever)