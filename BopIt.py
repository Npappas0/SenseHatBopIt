from Gyro import gyro
from score import score
from sense_hat import SenseHat
from random import randint
import time
sh = SenseHat()
sh.set_rotation(180)
g = gyro()
s = score("PlayerOne")
myList = ["Flip it", "Flick it", "Shake it"]
sh.show_message("Welcome to BopIt", scroll_speed=0.06, text_colour=[0,255,255])
time.sleep(1)
sh.show_message("Ready? Lets Go", scroll_speed=0.06, text_colour=[0,255,255])
gameOver = False

def command(n, g, gameOver):
    time.sleep(1)
    sh.show_message(myList[n], scroll_speed=0.03)
    k = 10
    while(k > 0 and gameOver == False):
        time.sleep(0.25)
        k -= 1
        if(n == 0 and g.flipped()):
            s.changeScore(1)
            gameOver = command(randint(0,2), g, gameOver)
        elif(n == 1):
            for event in sh.stick.get_events():
                if(event.action == 'pressed'):
                    s.changeScore(1)
                    gameOver = command(randint(0,2), g, gameOver)
        elif(n == 2 and g.shook()):
            s.changeScore(1)
            gameOver = command(randint(0,2), g, gameOver)
    if(gameOver == False):
        print("GameOver Your score was ")
        print(s.showScore())
        return True

command(randint(0,2), g, gameOver)

