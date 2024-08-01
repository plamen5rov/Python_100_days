from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("DeepPink3")

def draw_square():
    
    timmy_the_turtle.forward(120)
    for i in range(1,4):
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(120)
        
draw_square()







screen = Screen()
screen.exitonclick()