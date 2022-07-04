from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 3310")
screen.tracer(0)
print("test git")

# body_1 = Turtle()
# body_1.shape("square")
# body_1.color("white")
#
#
# body_2 = Turtle()
# body_2.penup()
# body_2.shape("square")
# body_2.color("white")
# body_2.goto(-20,0)
#
# body_3 = Turtle()
# body_3.penup()
# body_3.shape("square")
# body_3.color("white")
# body_3.goto(-40,0)
#

# starting_positions = [(0,0), (-20,0), (-40,0)]
# segments = []
#
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

screen.update()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # puts a delay between screen updates

    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    #detect collision with wall
    if (snake.head.xcor() > 285) or (snake.head.xcor() < -285) or (snake.head.ycor() >285) or (snake.head.ycor() < -285):
        game_is_on = False
        scoreboard.game_over()

    #detect collision with wall
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    #if head colllides with any segment in the tail:
    #   trigger game_ver











screen.exitonclick()