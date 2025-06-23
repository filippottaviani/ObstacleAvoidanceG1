from isaaclab.managers import RewardTermCfg, SceneEntityCfg
from isaaclab.utils import configclass
from isaaclab.envs import mdp
from managers.mdp import mdp_custom
import torch


@configclass
class RewardsCfg:

    # Vivo
    alive = RewardTermCfg(
        func=mdp.is_alive,
        weight=0.1
    )

    # In piedi
    standing = RewardTermCfg(
        func="isaaclab.envs.mdp.rewards:joint_pos_limits",
        params={
            "asset_cfg": SceneEntityCfg(
                name= "robot",
                joint_names= ["left_hip_pitch_joint","right_hip_pitch_joint"]
            )
        },
        weight=5.0
    )
    
    # Caduto
    fallen = RewardTermCfg(
        func=mdp_custom.has_fallen,
        params={
            "ref_link": "pelvis",
            "height_thr": 0.25 # soglia di altezza minima
        },
        weight=-5.0
    )
    
    # Cammina
    walking = RewardTermCfg(
        func=mdp_custom.moving,
        params={
            #"asset_cfg": SceneEntityCfg(name="robot"),
            "ref_link": "pelvis",
            "vel_thr": 0.5 # soglia di velocità minima
        },  
        weight=10.0
    )
    
    # Fuori dallo spazio di lavoro
    out_of_bounds = RewardTermCfg(
        func=mdp_custom.out_of_manual_bound,
        params={
            "max_dist": 5,  # limiti di giunzione
            "ref_link": "pelvis"  # link di riferimento per il controllo
        },
        weight=-2.0
    )

    # Colpisce un ostacolo
    hit_obstacle = RewardTermCfg(
        func=mdp.undesired_contacts,
        params={
            "threshold": 0.1,  # soglia di contatto
            "sensor_cfg": SceneEntityCfg(
                name="cont_sensor_LH"  # nome del sensore dell'ostacolo
            ),
        },
        weight=-2.0,
    )

    '''# Si avvicina all'obiettivo
    approach_goal = RewardTermCfg(
        func="isaaclab.envs.mdp.rewards:goal_distance",
        params={
            "asset_cfg": SceneEntityCfg(name="robot"),
            "target_cfg": SceneEntityCfg(name="goal"),
            "normalize": True,
        },
        weight=- torch.norm(robot.data.root_pos - self.target_position, dim=-1)
    )'''

    '''
    # Raggiunge l'obiettivo
    reach_goal = RewardTermCfg(
        func="isaaclab.envs.mdp.rewards:goal_reached",
        params={
            "asset_cfg": SceneEntityCfg(name="robot"),
            "target_cfg": SceneEntityCfg(name="goal"),
            "threshold": 0.3,
        },
        weight=100.0
    )
    '''