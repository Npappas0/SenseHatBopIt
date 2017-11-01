from Gyro import gyro
g = gyro()
g.update()
print(g.getRoll())
print(g.getPitch())
print(g.getYaw())

