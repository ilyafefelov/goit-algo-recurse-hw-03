import turtle


def draw_koch_segment(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        draw_koch_segment(t, order - 1, size)
        t.left(60)
        draw_koch_segment(t, order - 1, size)
        t.right(120)
        draw_koch_segment(t, order - 1, size)
        t.left(60)
        draw_koch_segment(t, order - 1, size)


def draw_koch_snowflake(t, order, size):
    for _ in range(3):
        draw_koch_segment(t, order, size)
        t.right(120)


def main():
    """
    This function is the entry point of the program. It prompts the user to enter the level of recursion,
    sets up the turtle graphics window, and calls the draw_koch_snowflake function to draw the snowflake.
    """
    while True:
        try:
            order = int(input("Enter the level of recursion: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    size = 600  # Increase the size of the snowflake

    screen = turtle.Screen()
    screen.title("Koch Snowflake")
    screen.bgcolor("yellow")  # Set the background color to blue

    t = turtle.Turtle()
    t.speed(10)  # Increase the turtle's speed
    t.pensize(3)  # Increase the turtle's pen size
    t.color("purple")  # Set the turtle's color to purple

    t.penup()
    t.goto(-300, 180)  # Adjust the starting position of the snowflake
    t.pendown()

    draw_koch_snowflake(t, order, size)

    screen.mainloop()


if __name__ == "__main__":
    main()
