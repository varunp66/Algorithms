import turtle

def draw_flower(ink):
    ink.up()
    ink.home()
    for degrees in range(10, 370, 10):
        ink.down()
        ink.forward(200)
        ink.up()
        ink.home()  # resets angle to 0 degrees
        ink.left(degrees)  # so absolute angle, not relative

def draw_stem(ink):
    ink.goto(1, -400)
    ink.home()
    ink.goto(5, -400)
    ink.home()
    ink.goto(3, -400)

def Draw():
    window = turtle.Screen()
    window.bgcolor("white")

    stem = turtle.Turtle()
    stem.color("green")
    stem.speed("fast")

    draw_stem(stem)

    flower = turtle.Turtle()
    flower.color("orange")
    flower.speed("fastest")

    draw_flower(flower)

Draw()

turtle.done()
