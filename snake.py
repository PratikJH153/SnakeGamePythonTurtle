from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        # Creates the snake body segments and appends in the Snake body List
        for i in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            if len(self.snake_body) == 0:
                self.snake_body.append(snake)
            else:
                snake.setx(self.snake_body[-1].pos()[0] - 20)
                self.snake_body.append(snake)

    def extend(self):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        position = self.snake_body[-1].pos()
        snake.goto(position[0], position[1])
        self.snake_body.append(snake)

    def move(self):
        """
        Moves the snake forward by 20 Pixels
        :return: Nothing
        """
        for parts_num in range(len(self.snake_body) - 1, 0, -1):
            (new_x, new_y) = self.snake_body[parts_num - 1].pos()
            self.snake_body[parts_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
