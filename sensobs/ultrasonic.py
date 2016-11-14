from sensobs.sensob import Sensob
from sensor_wrappers.ultrasonic_sensor import Ultrasonic

#Denne sesoren kan vi bruke til avoid collisions behavior sammen med irproximity
#update av denne sensoren returnerer avstanden til objekt foran i cm
#tenker at vi her kan returnere true hvis ovjekt fora er nærmere enn en
#viss lengde? Det kan lett brukes i behavior.

class Ultrasonic_sensob(Sensob):
    def __init__(self):
        super(Ultrasonic_sensob, self).__init__()
        self.sensor = Ultrasonic()

    def update(self, step = 0):
        if step % 3 == 0:
            values = self.sensor.update()
            print("VALUES:", values)
            #self.value = values[len(values)-1]