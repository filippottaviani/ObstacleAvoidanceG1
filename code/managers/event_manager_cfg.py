import math
from isaaclab.utils import configclass
from isaaclab.managers import EventTermCfg
from isaaclab.envs import mdp
from managers.mdp import mdp_custom

@configclass
class EventsCfg:

    # Uscita dallo spazio operativo
    out_of_bounds = EventTermCfg(
        func=mdp.reset_scene_to_default,
        mode="reset"
    )

    # Caduta del robot
    reset_on_fall = EventTermCfg(
        func=mdp.reset_scene_to_default,
        mode= "reset"
    )

    # Collisione con un ostacolo
    hit_obstacle = EventTermCfg(
        func=mdp.reset_scene_to_default,
        mode="reset"
    )

    '''# Raggiunge l'obiettivo
    reach_goal = EventTermCfg(
        func=mdp_custom.goal_reached,
        mode="reset"
    )'''

