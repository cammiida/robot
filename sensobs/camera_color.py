from sensobs.sensob import Sensob
from sensor_wrappers.camera import Camera

class Camera_color_sensob(Sensob):
    def __init__(self):
        super(Camera_color_sensob, self).__init__()
        self.sensor = Camera()

    def red_percentage(self, image):
        asd = {'rod': 0, 'gronn': 0, 'blaa': 0}

        for x in range(40,80):
            for y in range (40,50):
                rgb = image.getpixel((x, y))
                asd['rod'] += rgb[0]
                asd['gronn'] += rgb[1]
                asd['blaa'] += rgb[2]

        totalt = asd['rod'] + asd['gronn'] + asd['blaa']
        gronn = (asd['gronn'] / totalt) * 100
        blaa = (asd['blaa'] / totalt) * 100
        self.red = (asd['rod'] / totalt) * 100
        print("RGB:", self.red, gronn, blaa)
        if self.red > 2*gronn and self.red > 2*blaa:
            return True



    def update(self):
        value = self.sensor.update()
        return self.red_percentage(value)
