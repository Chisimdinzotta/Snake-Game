from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

level = screen.textinput(title="Choose your level", prompt="Hard, Normal, Easy:").lower()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
  screen.update()
 #set the game level; hard for fast, normal for normal pace and easy for slow
  snake.delay(level)
  snake.move()


  #Check collision with food using the distance turtle function
  #It checks the distance between the turtle and any parameter
  if snake.head.distance(food) < 17:
    #the food turtle was set to 10 by 10 remeber
    food.refresh()
    snake.extend()
    score.increase_score()

  #Detect collision with wall
  if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
    game_on = False
    score.game_over()

  #Detect collision with snake
  for segment in snake.segments[1:]:
    #the slicing uses everything in the segments except the head. We are checking against the head so we don't need
    #the head to check against itself

    if snake.head.distance(segment) < 10:
      game_on = False
      score.game_over()


screen.exitonclick()
