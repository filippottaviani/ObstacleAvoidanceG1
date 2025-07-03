import math
from isaaclab.utils import configclass
from isaaclab.managers import EventTermCfg
from isaaclab.envs import mdp

@configclass
class EventsCfg:

    # Riposizionamento del robot (resetta l'intera scena)
    robot_position_reset = EventTermCfg(
        func=mdp.reset_scene_to_default,
        mode="reset"
    )
