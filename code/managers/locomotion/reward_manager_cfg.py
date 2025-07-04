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
    
    '''# Caduto (hard)
    fallen_hard = RewardTermCfg(
        func=mdp_custom.has_fallen_hard,
        params={
            "ref_link": "pelvis",
            "thr": 0.5 
        },
        weight=-10.0
    )'''

    '''# Caduto (soft)
    fallen_soft = RewardTermCfg(
        func=mdp_custom.has_fallen_soft,
        params={
            "ref_link": "pelvis",
            "slope": 2 
        },
        weight=-10.0
    )'''

    '''# Caduto (tanh)
    fallen_tanh = RewardTermCfg(
        func=mdp_custom.has_fallen_tanh,
        params={
            "ref_link": "pelvis",
            "slope": 4 
        },
        weight=-2.0
    )'''

    '''# In piedi
    standing = RewardTermCfg(
        func=mdp_custom.standing,
        params={
            "ref_link": "pelvis",
            "sharpness": 100.0
        },
        weight=10.0
    )'''

    '''# Fuori dallo spazio di lavoro
    out_of_bounds = RewardTermCfg(
        func=mdp_custom.out_of_manual_bound,
        params={
            "max_dist": 5,  # limiti di giunzione
            "ref_link": "pelvis"  # link di riferimento per il controllo
        },
        weight=-1.0
    )'''

    '''# movimento in avanti
    moving_forward = RewardTermCfg(
        func=mdp_custom.moving,
        params={
            "ref_link": "pelvis"
        },
        weight=10.0
    )'''

    feet_air_time = RewardTermCfg(
        func=mdp.feet_air_time,
        params={
            "sensor_cfg": SceneEntityCfg(
                "contact_sensor_feet", 
                body_names=".*_ankle_roll_link"
            ),
            "command_name": "base_velocity",
            "threshold": 0.4,
        },
        weight=0.25
    )

    feet_slide = RewardTermCfg(
        func=mdp.feet_slide,
        params={
            "sensor_cfg": SceneEntityCfg(
                "contact_sensor_feet", 
                body_names=".*_ankle_roll_link"
            ),
            "asset_cfg": SceneEntityCfg(
                "robot", 
                body_names=".*_ankle_roll_link"
            ),
        },
        weight=-0.1
    )

    # Ricompense per il movimento
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

    # Penalità
    lin_vel_z_l2 = RewardTermCfg(
        func=mdp.lin_vel_z_l2,
        weight=-1.0
    )

    ang_vel_xy_l2 = RewardTermCfg(
        func=mdp.ang_vel_xy_l2, 
        weight=-0.05
    )

    dof_torques_l2 = RewardTermCfg(
        func=mdp.joint_torques_l2, 
        weight=-1.0e-5
    )

    dof_acc_l2 = RewardTermCfg(
        func=mdp.joint_acc_l2, 
        weight=-2.5e-7
    )

    # Penalize deviation from default of the joints that are not essential for locomotion
    joint_deviation_hip = RewardTermCfg(
        func=mdp.joint_deviation_l1,
        weight=-0.1,
        params={
            "asset_cfg": SceneEntityCfg(
                "robot", 
                joint_names=[
                    ".*_hip_yaw_joint",
                    ".*_hip_roll_joint"
                ]
            )
        },
    )
