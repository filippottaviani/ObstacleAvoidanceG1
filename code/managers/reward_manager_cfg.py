from isaaclab.managers import RewardTermCfg, SceneEntityCfg
from isaaclab.utils import configclass
from isaaclab.envs import mdp
from managers.mdp import mdp_rew_custom as mdp_custom


@configclass
class RewardsCfg:

    '''# Vivo
    alive = RewardTermCfg(
        func=mdp.is_alive,
        weight=0.1
    )'''

    '''# In piedi
    standing = RewardTermCfg(
        func="isaaclab.envs.mdp.rewards:joint_pos_limits",
        params={
            "asset_cfg": SceneEntityCfg(
                name= "robot",
                joint_names= ["left_hip_pitch_joint","right_hip_pitch_joint"]
            )
        },
        weight=0.1
    )'''
    
    # Caduto
    fallen = RewardTermCfg(
        func=mdp_custom.has_fallen,
        params={
            "ref_link": "pelvis",
            "height_thr": 0.25 # soglia di altezza minima
        },
        weight=-1.0
    )
    
    # Cammina
    walking = RewardTermCfg(
        func=mdp_custom.moving,
        params={
            #"asset_cfg": SceneEntityCfg(name="robot"),
            "ref_link": "pelvis",
            "vel_thr": 0.5 # soglia di velocità minima
        },  
        weight=0.2
    )
    
    # Fuori dallo spazio di lavoro
    out_of_bounds = RewardTermCfg(
        func=mdp_custom.out_of_manual_bound,
        params={
            "max_dist": 5,  # limiti di giunzione
            "ref_link": "pelvis"  # link di riferimento per il controllo
        },
        weight=-1.0
    )

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

    # Si avvicina all'obiettivo (penalità leggera)
    position_tracking_soft = RewardTermCfg(
        func=mdp_custom.position_error_tanh,
        params={
            "std": 2.0,
            "command_name": "target"
        },
        weight=1.0
    )

    # Si avvicina all'obiettivo (penalità negativa proporzionale)
    position_tracking_hard = RewardTermCfg(
        func=mdp_custom.position_error,
        params={
            "command_name": "target"
        },
        weight=-1.0,
    )

    # Obiettivo raggiunto
    reach_goal = RewardTermCfg(
        func=mdp_custom.target_reached,
        params={ 
            "command_name": "target",
            "threshold": 0.3
        },
        weight=10.0
    )