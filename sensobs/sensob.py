class Sensob:
    def __init__(self):
        self.sensors = []
        self.value = None

    def get_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()
"""
    def update(self):
        values = []

        for sensor in self.sensors:
            sensor.update()
            values.append(sensor.get_value())

        self.value = values
        return values

"""
