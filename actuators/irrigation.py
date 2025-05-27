class Irrigation:
    def __init__(self):
        self.on = False

    def control(self, temp, hum):
        if hum < 40:
            self.on = True
        elif hum > 60:
            self.on = False
