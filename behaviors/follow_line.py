from behaviors.behavior import Behavior
from sensobs.reflectance import Reflectance_sensob

thresh = 0.4

class Follow_line_behavior(Behavior):
    def __init__(self, reflectance_sensob = Reflectance_sensob()):
        super(Follow_line_behavior, self).__init__()
        self.sensobs = [reflectance_sensob]
        self.priority = 2

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        self.motor_recommendations = [(0, 0)]
        values = self.sensobs[0].value

        if (values[0] < thresh or values[1] < thresh):
            self.match_degree = 1
            self.motor_recommendations = [(1, -1)]
        elif (values[4] < thresh or values[5] < thresh):
            self.match_degree = 1
            self.motor_recommendations = [(-1, 1)]
        else:
            self.match_degree = 0.3
            self.motor_recommendations = [(0.5, 0.5)]