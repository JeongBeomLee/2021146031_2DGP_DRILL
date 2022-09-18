import turtle

count = 4

while count > 0:
    turtle.forward(500); turtle.left(90)
    count -= 1

turtle.forward(100); turtle.left(90)
turtle.forward(500); turtle.right(90)

turtle.forward(100); turtle.right(90)
turtle.forward(500); turtle.left(90)

turtle.forward(100); turtle.left(90)
turtle.forward(500); turtle.right(90)

turtle.forward(100); turtle.right(90)
turtle.forward(500); turtle.left(90)

turtle.home()

turtle.left(90); turtle.forward(100)
turtle.right(90); turtle.forward(500)

turtle.left(90); turtle.forward(100)
turtle.left(90); turtle.forward(500)

turtle.right(90); turtle.forward(100)
turtle.right(90); turtle.forward(500)

turtle.left(90); turtle.forward(100)
turtle.left(90); turtle.forward(500)

turtle.exitonclick()
