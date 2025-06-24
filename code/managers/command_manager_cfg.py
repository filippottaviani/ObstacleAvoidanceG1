from isaaclab.utils import configclass
from isaaclab.managers import CommandTermCfg
from scenes.basic_scenario import env_spacing
import isaaclab_tasks.manager_based.navigation.mdp as mdp_nav
import math

env_space = env_spacing

@configclass
class CommandsCfg:
    target = mdp_nav.UniformPose2dCommandCfg(
        asset_name="robot",
        resampling_time_range= (100.0, 100.0), # da sincronizzare con gli episodi?
        simple_heading=False,
        debug_vis=True,
        ranges=mdp_nav.UniformPose2dCommandCfg.Ranges(
            pos_x=(-env_space/2, env_space/2), 
            pos_y=(-env_space/2, env_space/2),  
            heading=(-math.pi, math.pi)
        )
    )
