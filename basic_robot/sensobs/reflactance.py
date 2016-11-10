from basic_robot.sensobs.sensob import Sensob
from basic_robot.sensor_wrappers.reflectance_sensors import ReflectanceSensors


#her skal vi ta inn verdi fra sensor og gjøre den om til en liste med to tall
#de tallene skal representere hvor linjen befinner seg under roboten
#dvs ved f.eks [0,2] så vil linjen mest sannsynelig være der og roboten
#bør da svinge til høyre
class Reflectance_sensob(Sensob):
    def __init__(self):
        super(Reflectance_sensob, self).__init__()
        self.sensors = [ReflectanceSensors()]

    def update(self):
        values = super(Reflectance_sensob, self).update()
        # så lag funksjon som finner ut hvor linjen mest snnsynlig er her