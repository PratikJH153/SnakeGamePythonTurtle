from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")

# To turn off the animation of snake moving forward as it causes distortion So, tracer(0) sets it to false
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.generate_food()
        scoreBoard.update_board()
        snake.extend()

    # Detect collision with wall
    if abs(snake.head.xcor()) >= 290 or abs(snake.head.ycor()) >= 290:
        game_is_on = False
        scoreBoard.game_over()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreBoard.game_over()


screen.exitonclick()
