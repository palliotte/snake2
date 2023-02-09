function rapple() {
    let index: number;
    
    let ok = 0
    apple.set(LedSpriteProperty.X, randint(0, 4))
    apple.set(LedSpriteProperty.Y, randint(0, 4))
    while (ok == 0) {
        n = 0
        index = 0
        while (index <= RINGS.length - 1) {
            if (RINGS[n].isTouching(apple)) {
                apple.set(LedSpriteProperty.X, randint(0, 4))
                apple.set(LedSpriteProperty.Y, randint(0, 4))
            } else {
                
            }
            
            index += 1
        }
    }
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (!(directionx == 0) && !(directiony == -1)) {
        directionx = 0
        directiony = 1
    }
    
})
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    
    if (!(directionx == 1) && !(directiony == 0)) {
        directionx = -1
        directiony = 0
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (!(directionx == 0) && !(directiony == 1)) {
        directionx = 0
        directiony = -1
    }
    
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    
    if (!(directionx == -1) && !(directiony == 0)) {
        directionx = 1
        directiony = 0
    }
    
})
let n = 0
let apple : game.LedSprite = null
let RINGS : game.LedSprite[] = []
let directionx = 1
let directiony = 0
game.setScore(0)
RINGS = [game.createSprite(1, 2), game.createSprite(0, 2)]
apple = game.createSprite(2, 2)
rapple()
basic.forever(function on_forever() {
    basic.pause(1000)
    RINGS.unshift(game.createSprite(RINGS[0].get(LedSpriteProperty.X) + directionx, RINGS[0].get(LedSpriteProperty.Y) + directiony))
    if (RINGS[0].isTouchingEdge()) {
        if (RINGS[0].get(LedSpriteProperty.X) == 0 && directionx == -1 || RINGS[0].get(LedSpriteProperty.X) == 4 && directionx == 1 || RINGS[0].get(LedSpriteProperty.Y) == 0 && directiony == -1 || RINGS[0].get(LedSpriteProperty.Y) == 4 && directionx == 1) {
            game.gameOver()
        }
        
    }
    
    if (RINGS[0].isTouching(apple)) {
        rapple()
        game.addScore(1)
    } else {
        RINGS[RINGS.length - 1].delete()
        RINGS.removeAt(RINGS.length - 1)
    }
    
})
