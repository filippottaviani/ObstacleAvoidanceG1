from isaaclab.managers import RewardTermCfg, SceneEntityCfg
from isaaclab.utils import configclass
from isaaclab.envs import mdp
from managers.mdp import mdp_rew_custom as mdp_custom
import isaaclab_tasks.manager_based.locomotion.velocity.mdp as mdp
import math


@configclass
class RewardsCfg:

    # Limita il nervosismo delle azioni
    action_rate_l2 = RewardTermCfg(
        func=mdp.action_rate_l2,
        weight=-0.05
    )

    # In piedi
    standing = RewardTermCfg(
        func=mdp_custom.standing,
        params={
            "ref_link": "pelvis"
        },
        weight=5.0
    )
    
    # Caduto [DA SISTEMARE]
    fallen = RewardTermCfg(
        func=mdp_custom.has_fallen,
        params={
            "ref_link": "pelvis",
            "height_thr": 0.3 # soglia di altezza minima
        },
        weight=-1.0
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

    '''# Assecondare il sollevamento del piede destro
    feet_air_time_R = RewardTermCfg(
        func=mdp.feet_air_time,
        params={
            "sensor_cfg": SceneEntityCfg(
                "contact_sensor_feet", 
                body_names="right_ankle_roll_link"
            ),
            "command_name": "target",
            "threshold": 0.5,
        },
        weight=2.0
    )
'''
    '''# Assecondare il sollevamento del piede sinistro
    feet_air_time_L = RewardTermCfg(
        func=mdp.feet_air_time,
        params={
            "sensor_cfg": SceneEntityCfg(
                "contact_sensor_feet", 
                body_names="left_ankle_roll_link"
            ),
            "command_name": "target",
            "threshold": 0.5,
        },
        weight=2.0
    )'''

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
    )

    # Obiettivo raggiunto
    reach_goal = RewardTermCfg(
        func=mdp_custom.target_reached,
        params={ 
            "command_name": "target",
            "threshold": 0.3
        },
        weight=100.0
    )'''