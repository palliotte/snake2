function apple_random() {
    
    while (ok == 0) {
        index = 0
        while (index <= RINGS.length - 1) {
            if (apple.isTouching(RINGS[index])) {
                apple.set(LedSpriteProperty.X, randint(0, 4))
                apple.set(LedSpriteProperty.Y, randint(0, 4))
            } else {
                ok = 1
            }
            
            index += 1
        }
    }
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    directionx = 0
    directiony = 1
})
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    
    directionx = -1
    directiony = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    directionx = 0
    directiony = -1
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    
    directionx = 1
    directiony = 0
})
let index = 0
let ok = 0
let apple : game.LedSprite = null
let directiony = 0
let directionx = 0
let RINGS : game.LedSprite[] = []
game.setScore(0)
RINGS = [game.createSprite(1, 2), game.createSprite(0, 2)]
directionx = 1
directiony = 1
apple = game.createSprite(2, 2)
ok = 0
apple_random()
basic.forever(function on_forever() {
    basic.pause(1000)
    RINGS.unshift(game.createSprite(RINGS[0].get(LedSpriteProperty.X) + directionx, RINGS[0].get(LedSpriteProperty.Y) + directiony))
    //     if RINGS[0].is_touching_edge():
    //         game.game_over()
    if (RINGS[0].isTouching(apple)) {
        game.addScore(1)
        apple_random()
    } else {
        RINGS[RINGS.length - 1].delete()
        _py.py_array_pop(RINGS)
    }
    
})
