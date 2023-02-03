input.onButtonPressed(Button.A, function () {
    directionx = 0
    directiony = 1
})
input.onGesture(Gesture.TiltLeft, function () {
    directionx = -1
    directiony = 0
})
function apple_random () {
    while (ok == 0) {
        for (let index = 0; index <= RINGS.length; index++) {
            if (apple.isTouching(RINGS[index])) {
                apple.set(LedSpriteProperty.X, randint(0, 4))
                apple.set(LedSpriteProperty.Y, randint(0, 4))
            } else {
                ok = 1
            }
        }
    }
}
input.onButtonPressed(Button.B, function () {
    directionx = 0
    directiony = -1
})
input.onGesture(Gesture.TiltRight, function () {
    directionx = 1
    directiony = 0
})
let ok = 0
let apple: game.LedSprite = null
let directiony = 0
let directionx = 0
let RINGS: game.LedSprite[] = []
game.setScore(0)
RINGS = [game.createSprite(0, 2)]
directionx = 1
directiony = 1
apple = game.createSprite(2, 2)
ok = 0
apple_random()
basic.forever(function () {
    basic.pause(1000)
    RINGS.unshift(game.createSprite(RINGS[0].get(LedSpriteProperty.X) + directionx, RINGS[0].get(LedSpriteProperty.Y) + directiony))
    if (RINGS[0].isTouchingEdge()) {
        game.gameOver()
    }
    if (RINGS[0].isTouching(apple)) {
        game.addScore(1)
        apple_random()
    } else {
        RINGS.pop()
    }
})
