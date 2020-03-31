import turtle

num_squares = 100
side = side_unit = 30

for sq in range (100):
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    side = side_unit + 3 * sq

    turtle.goto(0,0)

turtle.done
    
