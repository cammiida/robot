from basic_robot.behaviors.behavior import Behavior
from sensobs.front_distance import Front_distance_sensob
from sensobs.ir import IR_sensob


class Avoid_collisions_behavior(Behavior):
    def __init__(self, distance_sensob = Front_distance_sensob(), ir_sensob=IR_sensob()):
        super(Avoid_collisions_behavior, self).__init__()
        self.sensobs = [distance_sensob, ir_sensob]

        self.priority = 1

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        dist = self.sensobs[0].value

        ir = self.sensobs[1].value

        if ir[0]:
            self.motor_recommendations = [(1, -1)]
            self.match_degree = 1
        elif ir[1]:
            self.motor_recommendations = [(-1, 1)]
            self.match_degree = 1
        elif dist > 15:
            self.motor_recommendations = [(0.5, 0.5)]
            self.match_degree = 0.1
        else:
            # turn right
            self.motor_recommendations = [(1, -1)]
            self.match_degree = 1