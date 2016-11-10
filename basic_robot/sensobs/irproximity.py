from basic_robot.sensobs.sensob import Sensob
from basic_robot.sensor_wrappers.irproximity_sensor import IRProximitySensor
#Denne sesoren kan vi bruke til avoid collisions behavior sammen med ultrasonic
#update av denne sensoren returnerer true hvis avstanden til ting på siden
# er nærmere enn ca 3 cm, da kan vi bare få den til å svinge litt sånn eller noe


class IRProximity_sensob(Sensob):
    def __init__(self):
        super(IRProximity_sensob, self).__init__()
        self.sensor = IRProximitySensor()

    def update(self):
        self.value = super(IRProximity_sensob, self).update()
        print("IRProximity:", self.value)
