from isaaclab.managers import RewardTermCfg, SceneEntityCfg
from isaaclab.utils import configclass
from isaaclab.envs import mdp
from managers.mdp import mdp_rew_custom as mdp_custom
import isaaclab_tasks.manager_based.locomotion.velocity.mdp as mdp
import isaaclab.envs.mdp.rewards as mdp1
import math


@configclass
class RewardsCfg:

    '''alive = RewardTermCfg(
        func=mdp.is_alive, 
        weight=0.5
    )'''

    # Limita il nervosismo delle azioni
    action_rate_l2 = RewardTermCfg(
        func=mdp.action_rate_l2,
        weight=-0.01 
    )

    '''# In piedi
    standing = RewardTermCfg(
        func=mdp_custom.standing,
        params={
            "ref_link": "pelvis",
            "tol": 15.0
        },
        weight=10.0
    )'''

    '''
    # Caduto
    fallen = RewardTermCfg(
        func=mdp_custom.has_fallen,
        params={
            "ref_link": "pelvis",
            "thr": 0.5 
        },
        weight=-50.0
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
        weight=0.125,
        params={
            "sensor_cfg": SceneEntityCfg(
                "contact_sensor_feet", 
                body_names=".*_ankle_roll_link"
            ),
            "command_name": "base_velocity",
            "threshold": 0.5,
        },
    )

       # -- task
    track_lin_vel_xy_exp = RewardTermCfg(func=mdp.track_lin_vel_xy_exp, weight=1.0, params={"command_name": "base_velocity", "std": math.sqrt(0.25)})
    track_ang_vel_z_exp = RewardTermCfg(func=mdp.track_ang_vel_z_exp, weight=0.5, params={"command_name": "base_velocity", "std": math.sqrt(0.25)})

    # -- penalties
    lin_vel_z_l2 = RewardTermCfg(func=mdp.lin_vel_z_l2, weight=-2.0)
    ang_vel_xy_l2 = RewardTermCfg(func=mdp.ang_vel_xy_l2, weight=-0.05)
    dof_torques_l2 = RewardTermCfg(func=mdp.joint_torques_l2, weight=-1.0e-5)
    dof_acc_l2 = RewardTermCfg(func=mdp.joint_acc_l2, weight=-2.5e-7)

    '''# Colpisce un ostacolo
    hit_obstacle = RewardTermCfg(
        func=mdp.undesired_contacts,
        params={
            "threshold": 0.1,  # soglia di contatto
            "sensor_cfg": SceneEntityCfg(
                name="cont_sensor_LH"  # nome del sensore dell'ostacolo
            ),
        },
        weight=-0.5,
    )'''

    '''# Va nella direzioned dell'obiettivo
    heading_tracking= RewardTermCfg(
        func=mdp_custom.heading_error,
        params={
            "command_name": "target"
        },
        weight=1.0
    )'''

    '''# Si avvicina all'obiettivo
    position_tracking = RewardTermCfg(
        func=mdp_custom.position_error,
        params={
            "command_name": "target"
        },
        weight=-1.0,
    )'''

    '''# Obiettivo raggiunto
    reach_goal = RewardTermCfg(
        func=mdp_custom.target_reached,
        params={ 
            "command_name": "target",
            "threshold": 0.3
        },
        weight=100.0
    )'''