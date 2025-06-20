import math
from isaaclab.utils import configclass
from isaaclab.managers import EventTermCfg, SceneEntityCfg
from isaaclab.envs import mdp

@configclass
class EventsCfg:

    # caduta
    terminate_on_fall = EventTermCfg(
        func=mdp.reset_scene_to_default,
        mode="reset"
    )

    # uscita dal box operativo
    terminate_on_out_of_bounds = EventTermCfg(
        func=mdp.reset_scene_to_default,
        mode="reset"
    )
