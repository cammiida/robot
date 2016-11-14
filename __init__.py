from arbitrator import Arbitrator
from BBCON import BBCON
from behaviors.avoid_collisions import Avoid_collisions_behavior
from motob import Motob
from motors import Motors
from sensobs.ultrasonic import Ultrasonic_sensob
from zumo_button import ZumoButton

if __name__ == '__main__':
    ZumoButton().wait_for_press()
    #sensobs
    distance_sensob = Ultrasonic_sensob()
    sensobs = [distance_sensob]

    # behaviors
    avoid_collisions = Avoid_collisions_behavior(distance_sensob)
    behaviors = [avoid_collisions]

    # motobs
    motors = [Motors()]
    motob = Motob(motors)
    motobs = [motob]

    # arbitrator
    arbitrator = Arbitrator()

    bbcon = BBCON(behaviors, sensobs, motobs, arbitrator)
    bbcon.activate_behavior(avoid_collisions)
    arbitrator.bbcon = bbcon

    while True:
        pass
        bbcon.run_one_timestep()
