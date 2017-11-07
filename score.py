class score:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def changeScore(self, score):
        self.score = self.score + score

    def resetScore(self):
        self.score = 0

    def showScore(self):
        return self.score

    def changeName(self,name):
        self.name = name

    def showName(self):
        return self.name
