from Gyro import gyro
from sense_hat import SenseHat
from random import randint
g = gyro()
s = SenseHat()
myList = ["Rotate It", "Flick It", "Flip It"]
s.show_message("H")
randNum = randint(0,2)
print(myList[randNum])

if(randNum == 0):
    

g.update()
print(g.getRoll())
print(g.getPitch())
print(g.getYaw())

