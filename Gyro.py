from sense_hat import SenseHat
class gyro:
    def __init__(self):
        self.roll = 0
        self.pitch = 0
        self.yaw = 0

    def update(self):
        sense = SenseHat()
        sense.clear()
        o = sense.get_orientation()
        self.pitch = o["pitch"]
        self.roll = o["roll"]
        self.yaw = o["yaw"]
        
    def getRoll(self):
        return self.roll

    def getPitch(self):
        return self.pitch

    def getYaw(self):
        return self.yaw
