from sense_hat import SenseHat
class gyro:
    def __init__(self):
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.aroll = 0
        self.apitch = 0
        self.ayaw = 0

    def update(self):
        sense = SenseHat()
        sense.clear()
        o = sense.get_orientation()
        a = sense.get_accelerometer()
        self.pitch = o["pitch"]
        self.roll = o["roll"]
        self.yaw = o["yaw"]
        self.apitch = a["pitch"]
        self.aroll = a["roll"]
        self.ayaw = a["yaw"]
        
    def getRoll(self):
        return self.roll

    def getPitch(self):
        return self.pitch

    def getYaw(self):
        return self.yaw

    def getaRoll(self):
        return self.aroll

    def getaPitch(self):
        return self.apitch

    def getaYaw(self):
        return self.ayaw

    def flipped(self):
        self.update()
        if(self.getRoll() > 160 and self.getRoll() < 200):
            return True

    def shook(self):
        self.update()
        if(self.getaYaw() > 160 and self.getaYaw() < 200):
            return True
