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

def apple_random():
    global ok
    while ok == 0:
        index = 0
        while index <= len(list2):
            if apple.is_touching(list2[index]):
                apple.set(LedSpriteProperty.X, randint(0, 4))
                apple.set(LedSpriteProperty.Y, randint(0, 4))
            else:
                ok = 1
            index += 1

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

ok = 0
apple: game.LedSprite = None
directiony = 0
directionx = 0
list2: List[game.LedSprite] = []
game.set_score(0)
list2 = [game.create_sprite(0, 2)]
directionx = 1
directiony = 1
apple = game.create_sprite(2, 2)
ok = 0
apple_random()

def on_forever():
    basic.pause(1000)
    list2.unshift(game.create_sprite(list2[0].get(LedSpriteProperty.X) + directionx,
            list2[0].get(LedSpriteProperty.Y) + directiony))
    if list2[0].is_touching_edge():
        game.game_over()
    if list2[0].is_touching(apple):
        game.add_score(1)
        apple_random()
    else:
        list2.pop()
basic.forever(on_forever)
