import turtle
turtle.showturtle()
for x in range(0,200):
    turtle.forward(20)
    c = x%2
    if c == 0:
        turtle.left(-2*x)
    else:
        turtle.right(2*x)
    
