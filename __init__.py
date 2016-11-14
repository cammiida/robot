from arbitrator import Arbitrator
from BBCON import BBCON
from behaviors.avoid_collisions import Avoid_collisions_behavior
from behaviors.follow_line import Follow_line_behavior
from motob import Motob
from motors import Motors
from sensobs.ultrasonic import Ultrasonic_sensob
from sensobs.camera_color import Camera_color_sensob
from sensobs.reflectance import Reflectance_sensob
from sensobs.irproximity import IRProximity_sensob
from zumo_button import ZumoButton

if __name__ == '__main__':
    ZumoButton().wait_for_press()
    # sensobs
    distance_sensob = Ultrasonic_sensob()
    colors_sensob = Camera_color_sensob()
    reflectance_sensob = Reflectance_sensob()
    ir_sensob = IRProximity_sensob()
    sensobs = [distance_sensob, reflectance_sensob, colors_sensob, ir_sensob]

    # behaviors
    avoid_collisions = Avoid_collisions_behavior(distance_sensob, ir_sensob)
    follow_line = Follow_line_behavior(reflectance_sensob)
    behaviors = [avoid_collisions, follow_line]

    # motobs
    motors = [Motors()]
    motob = Motob(motors)
    motobs = [motob]

    # arbitrator
    arbitrator = Arbitrator()

    bbcon = BBCON(behaviors, sensobs, motobs, arbitrator)
    bbcon.activate_behavior(avoid_collisions)
    bbcon.activate_behavior(follow_line)
    arbitrator.bbcon = bbcon

    while True:
        bbcon.run_one_timestep()
