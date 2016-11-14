from sensobs.sensob import Sensob
from sensor_wrappers.camera import Camera
from imager2 import Imager


class Camera_color_sensob(Sensob):
    def __init__(self):
        super(Camera_color_sensob, self).__init__()
        self.sensors = [Camera()]

    def update(self):
        values = super(Camera_color_sensob, self).update()
        self.value = Imager().map_color_wta(image=values[0],thresh=0.50).get_red_percentage()
