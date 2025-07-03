from isaaclab.utils import configclass
from scenes.basic_scenario import env_spacing
import isaaclab_tasks.manager_based.navigation.mdp as mdp_nav
import isaaclab_tasks.manager_based.locomotion.velocity.mdp as mdp_vel
import math


@configclass
class CommandsCfg:
    '''target = mdp_nav.UniformPose2dCommandCfg(
        asset_name="robot",
        resampling_time_range= (50.0, 100.0), # da sincronizzare con gli episodi?
        simple_heading=False,
        debug_vis=True,
        ranges=mdp_nav.UniformPose2dCommandCfg.Ranges(
            pos_x=(-env_spacing/2, env_spacing/2), 
            pos_y=(-env_spacing/2, env_spacing/2),  
            heading=(-math.pi, math.pi)
        )
    )'''

    base_velocity = mdp_vel.UniformVelocityCommandCfg(
        asset_name="robot",
        resampling_time_range=(10.0, 10.0),
        rel_standing_envs=0.02,
        rel_heading_envs=1.0,
        heading_command=True,
        heading_control_stiffness=0.5,
        debug_vis=True,
        ranges=mdp_vel.UniformVelocityCommandCfg.Ranges(
            lin_vel_x=(-1.0, 1.0), 
            lin_vel_y=(-1.0, 1.0), 
            ang_vel_z=(-1.0, 1.0), 
            heading=(-math.pi, math.pi)
        ),
    )
