input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    directionx = 0
    directiony = 1
    direx = directionx
    direy = directiony
})
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    
    direx = directionx
    direy = directiony
    directionx = -1
    directiony = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    direx = directionx
    direy = directiony
    directionx = 0
    directiony = -1
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    
    direx = directionx
    direy = directiony
    directionx = 1
    directiony = 0
})
function rapple() {
    let n: number;
    let ok = 0
    while (ok == 0) {
        n = 0
        for (n = 0; n < RINGS.length - 1; n++) {
            apple.set(LedSpriteProperty.X, randint(0, 4))
            apple.set(LedSpriteProperty.Y, randint(0, 4))
            if (!apple.isTouching(RINGS[n])) {
                ok = 1
            }
            
        }
    }
}

let direy = 0
let direx = 1
let directiony = 0
let directionx = 1
game.setScore(0)
let RINGS = [game.createSprite(1, 2), game.createSprite(0, 2)]
let apple = game.createSprite(2, 2)
rapple()
basic.forever(function on_forever() {
    
    basic.pause(1000)
    RINGS.unshift(game.createSprite(RINGS[0].get(LedSpriteProperty.X) + directionx, RINGS[0].get(LedSpriteProperty.Y) + directiony))
    RINGS[RINGS.length - 1].delete()
    RINGS.removeAt(RINGS.length - 1)
})
