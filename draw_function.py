import turtle as t

x_min = -5
x_max = 5

y_min = -5
y_max = 5

space = 0.1
fun1 = "y = abs(x)"
fun2 = "y = x*x"
fun3 = "y = 0.5*x + 1"

t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.pensize(2)

t.up()
t.goto(x_min,0)
t.down()
t.goto(x_max,0)

t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)


x = x_min
exec(fun1)
t.up()
t.goto(x,y)
t.down()
while x <= x_max:
    x = x + space
    exec(fun1)
    t.goto(x,y)

x = x_min
exec(fun2)
t.up()
t.goto(x,y)
t.down()
while x<=x_max:
    x = x+space
    exec(fun2)
    t.goto(x,y)

x = x_min

exec(fun3)
t.up()
t.goto(x,y)
t.down()
while x<=x_max:
    x=x+space
    exec(fun3)
    t.goto(x,y)