import turtle as t

t.bgcolor("black")

for i in range(3):
    if i % 3 == 0:
        t.color("red")
    if i % 3 == 1:
        t.color("yellow")
    if i %3 == 2:
        t.color("blue")
    t.forward(100)
    t.left(120)