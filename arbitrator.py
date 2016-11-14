


class Arbitrator:

    def __init__(self):
        self.bbcon = None

    def choose_action(self):
        halt = False
        best_behavior = self.bbcon.active_behaviors[0]
        for behavior in self.bbcon.active_behaviors:
            if behavior.weight > best_behavior.weight:
                best_behavior = behavior


        return best_behavior.motor_recommendations, best_behavior.halt_request