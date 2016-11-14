

class Behavior:
    def __init__(self):
        self.bbcon = None
        self.sensobs = []
        self.motor_recommendations = []
        self.active_flag = False
        self.halt_request = False
        self.priority = 1 # static

        self.match_degree = 0.5

    @property
    def weight(self):
        return self.priority * self.match_degree

    def consider_deactivation(self):
        if False:
            self.active_flag = False

    def consider_activation(self):
        if False:
            self.active_flag = True

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if not self.active_flag:
            # tell sensobs we're not active
            return
        # tell sensobs we're active
        self.sense_and_act()

    def sense_and_act(self):
        # calculate motor_recommendations, halt_request and match_degree
        # based on sensob values
        pass