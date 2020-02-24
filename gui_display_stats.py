import turtle


def window():
    wn = turtle.Screen()
    wn.title("I love you Mom. <3")
    wn.bgcolor("grey")
    wn.setup(width=800, height=600)


def draw_num(string_ip, x=0, y=0, color="white", size=15):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color(color)
    pen.penup()
    pen.hideturtle()
    pen.goto(x, y)
    pen.write(string_ip, align="center", font=("Comic Sans", size, "normal"))


def draw_square(side_length_x, side_length_y, x=0, y=0, color="black"):
    square = turtle.Turtle()
    square.penup()
    square.speed(0)
    square.color(color)
    square.hideturtle()
    square.goto(x, y)
    square.shape("turtle")
    square.pendown()
    square.forward(side_length_x)
    square.left(90)
    square.forward(side_length_y)
    square.left(90)
    square.forward(side_length_x)
    square.left(90)
    square.forward(side_length_y)
    square.right(90)


def draw_row(forward_x, x=0, y=0, color="black"):
    row = turtle.Turtle()
    row.penup()
    row.speed(0)
    row.color(color)
    row.hideturtle()
    row.goto(x, y)
    row.shape("turtle")
    row.pendown()
    row.forward(forward_x)
    row.left(0)
    row.forward(forward_x)


def draw_rows(forward_x, x=0, y=0, color="black"):
    displacement = 300
    loop_len = 0
    while loop_len < 10:
        displacement -= 30
        draw_row(forward_x / 2, x, y + displacement, color)
        loop_len += 1
        print(forward_x)


def draw_grid(side_length_x, side_length_y, x=0, y=0, color="black"):
    draw_square(side_length_x, side_length_y, x, y, color)
    draw_rows(side_length_x, x, y, color)

def keep_open():
    turtle.mainloop()