from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


tim = Turtle()
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))





screen.tracer(0)

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("welcome to the pong game !")
screen.listen()
screen.onkey(paddle_l.up,"w")
screen.onkey(paddle_l.down,"s")
screen.onkey(paddle_r.up,"i")
screen.onkey(paddle_r.down,"k")

screen. update()


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    ball.move()

    #detect collision with ball
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.bounce_y()

    #detect collision with ball paddle
    if (ball.distance(paddle_r)  < 50 and ball.xcor() > 320) or (ball.distance(paddle_l)  < 50 and ball.xcor() < -320):
        ball.bounce_x()


    #detech r paddle misses
    if ball.xcor() > 380 :
       ball.reset_position()
       scoreboard.l_point()
       scoreboard.update_scoreboard()


    #detech l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()


    screen.update()


screen.exitonclick()







