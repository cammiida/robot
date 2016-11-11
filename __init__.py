from basic_robot.arbitrator import Arbitrator
from basic_robot.BBCON import BBCON
#from basic_robot.behaviors.avoid_collisions import Avoid_collisions_behavior #ikke laget
from basic_robot.motob import Motob
from basic_robot.motors import Motors
#from basic_robot.sensobs.front_distance import Front_distance_sensob #ikke laget
from basic_robot.zumo_button import ZumoButton

if __name__ == '__main__':
    ZumoButton().wait_for_press()
    # sensobs
    #distance_sensob = Front_distance_sensob()
    #sensobs = [distance_sensob]

    # behaviors
    #avoid_collisions = Avoid_collisions_behavior(distance_sensob)
    #behaviors = [avoid_collisions]

    # motobs
    motors = [Motors()]
    motob = Motob(motors)
    motobs = [motob]

    # arbitrator
    arbitrator = Arbitrator()

    #bbcon = BBCON(behaviors, sensobs, motobs, arbitrator)
    #bbcon.activate_behavior(avoid_collisions)
    #arbitrator.bbcon = bbcon

    while True:
        pass
        #bbcon.run_one_timestep()
