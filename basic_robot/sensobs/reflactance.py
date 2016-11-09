from basic_robot.sensobs.sensob import Sensob
from basic_robot.sensor_wrappers.reflectance_sensors import ReflectanceSensors


class Reflectance_sensob(Sensob):
    def __init__(self):
        super(Reflectance_sensob, self).__init__()
        self.sensors = [ReflectanceSensors()]

    def update(self):
        values = super(Reflectance_sensob, self).update()
        self.value = values[0]
        print('reflectance', self.value)