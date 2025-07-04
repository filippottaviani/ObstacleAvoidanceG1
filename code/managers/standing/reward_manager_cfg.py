from isaaclab.managers import RewardTermCfg, SceneEntityCfg
from isaaclab.utils import configclass
from isaaclab.envs import mdp
from managers.mdp import mdp_rew_custom as mdp_custom
import isaaclab_tasks.manager_based.locomotion.velocity.mdp as mdp
import isaaclab.envs.mdp.rewards as mdp1
import math


@configclass
class RewardsCfg:

    alive = RewardTermCfg(
        func=mdp.is_alive, 
        weight=0.5
    )

    termination_penalty = RewardTermCfg(
        func=mdp.is_terminated,
        weight=-200.0
    )

    '''# Limita il nervosismo delle azioni
    action_rate_l2 = RewardTermCfg(
        func=mdp.action_rate_l2,
        weight=-0.01 
    )'''

    '''# Limita la forza delle azioni
    action_l2 = RewardTermCfg(
        func=mdp.action_l2,
        weight=-0.01 
    )'''

    # In piedi
    standing = RewardTermCfg(
        func=mdp_custom.standing,
        params={
            "ref_link": "pelvis",
            "sharpness": 100.0
        },
        weight=10.0
    )

    # Ricompense per il (non) movimento
    track_lin_vel_xy_exp = RewardTermCfg(
        func=mdp.track_lin_vel_xy_exp, 
        params={
            "command_name": "base_velocity", 
            "std": math.sqrt(0.25)
        },
        weight=1.0
    )

    track_ang_vel_z_exp = RewardTermCfg(
        func=mdp.track_ang_vel_z_exp,  
        params={
            "command_name": "base_velocity", 
            "std": math.sqrt(0.25)
        },
        weight=2.0,
    )
