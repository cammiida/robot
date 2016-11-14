from sensobs.sensob import Sensob
from sensor_wrappers.camera import Camera
from imager2 import Imager


class Camera_color_sensob(Sensob):
    def __init__(self):
        super(Camera_color_sensob, self).__init__()
        self.sensors = [Camera()]

    def red_percentage(self, image):
        rgbs =0

        for x in range(40,80):
            rgb = image.get_pixel(x, 48)
            i = rgb.index(max(rgb))
            if i == 0:
                rgbs += 1

        self.red = (rgbs / 40) * 100


    def update(self):
        values = super(Camera_color_sensob, self).update()
        self.red_percentage(Imager(values[0]))
        return self.red > 20
