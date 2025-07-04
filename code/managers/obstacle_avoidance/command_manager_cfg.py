from isaaclab.utils import configclass
from task.obstacle_avoidance.oa_env_config import ObstacleAvoidanceEnvCfg
import isaaclab_tasks.manager_based.navigation.mdp as mdp
import math


@configclass
class CommandsCfg:
    env_spacing = ObstacleAvoidanceEnvCfg.env_spacing
    target = mdp.UniformPose2dCommandCfg(
        asset_name="robot",
        resampling_time_range= (50.0, 100.0), # da sincronizzare con gli episodi?
        simple_heading=False,
        debug_vis=True,
        ranges=mdp.UniformPose2dCommandCfg.Ranges(
            pos_x=(-env_spacing/2, env_spacing/2), 
            pos_y=(-env_spacing/2, env_spacing/2),  
            heading=(-math.pi, math.pi)
        )
    )
