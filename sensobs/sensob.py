class Sensob:
    def __init__(self):
        self.sensors = []
        self.value = None

    def get_value(self):
        return self.value

    def update(self):
        pass

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()