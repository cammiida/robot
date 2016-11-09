import time


class BBCON:
    def __init__(self, behaviors, sensobs, motobs, arbitrator):
        self.behaviors = behaviors
        self.active_behaviors = []
        self.sensobs = sensobs
        self.motobs = motobs
        self.arbitrator = arbitrator

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        if behavior not in self.behaviors:
            raise Exception('Behavior not used by this BBCON')

        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        for sensob in self.sensobs:
            sensob.update()


        for behavior in self.behaviors:
            behavior.update()
            if behavior.active_flag:
                self.activate_behavior(behavior)
            else:
                self.deactivate_behavior(behavior)

        recommendations, stop = self.arbitrator.choose_action()
        for i in range(len(self.motobs)):
            self.motobs[i].update(recommendations[i])

        time.sleep(0.5)

        for sensob in self.sensobs:
            sensob.reset()


