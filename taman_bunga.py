import turtle
import math
import time

# Setup layar
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.bgcolor("skyblue")
screen.title("Taman Bunga Bergerak 🌸")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Gambar rumput
def draw_grass():
    t.penup()
    t.goto(-450, -250)
    t.pendown()
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(900)
        t.right(90)
        t.forward(250)
        t.right(90)
    t.end_fill()

# Gambar bunga
def draw_flower(x, y, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(90 + angle)
    t.pendown()

    # Batang
    t.color("darkgreen")
    t.pensize(5)
    t.forward(90)

    # Kelopak
    t.color("pink")
    t.pensize(2)
    for _ in range(6):
        t.circle(18)
        t.right(60)

    # Tengah bunga
    t.penup()
    t.forward(10)
    t.color("yellow")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

# Posisi bunga
flowers = [-300, -150, 0, 150, 300]

# Animasi
while True:
    t.clear()
    draw_grass()

    angle = math.sin(time.time() * 2) * 12  # efek angin
    for x in flowers:
        draw_flower(x, -250, angle)

    screen.update()
    time.sleep(0.03)
