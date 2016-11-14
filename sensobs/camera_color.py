from sensobs.sensob import Sensob
from sensor_wrappers.camera import Camera


class Camera_color_sensob(Sensob):
    def __init__(self):
        super(Camera_color_sensob, self).__init__()
        self.sensors = [Camera()]

    def update(self):
        values = super(Camera_color_sensob, self).update()
        self.value = values[0].map_color_wta(thresh=0.50).get_red_percentage()
