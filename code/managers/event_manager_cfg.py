import math
from isaaclab.utils import configclass
from isaaclab.managers import EventTermCfg
from isaaclab.envs import mdp
from managers.mdp import mdp_custom

@configclass
class EventsCfg:

    '''# uscita dal box operativo
    terminate_on_out_of_bounds = EventTermCfg(
        func=mdp.reset_scene_to_default,
        mode="reset"
    )'''
