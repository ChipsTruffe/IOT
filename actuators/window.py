class Window:
    def __init__(self):
        self.open = False

    def control(self, temp, hum):
        if temp > 30:
            self.open = True
        elif temp < 25:
            self.open = False
