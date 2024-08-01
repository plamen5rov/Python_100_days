from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("DeepPink3")

def draw_square():
    tim.forward(120)
    for i in range(1,4):
        tim.right(90)
        tim.forward(120)
        
# draw_square()

def draw_dashed_line(length):
    for _ in range(1, length):
        tim.color("black")
        tim.forward(5)
        tim.color("white")
        tim.forward(5)
        

     

def draw_dashed_line2(length):
    for _ in range(length):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
    

# draw_dashed_line(25)

# tim.right(90)

draw_dashed_line2(55)




screen = Screen()
screen.exitonclick()