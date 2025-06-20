from isaaclab.managers import RewardTermCfg, SceneEntityCfg
from isaaclab.utils import configclass
from isaaclab.envs import mdp


@configclass
class RewardsCfg:

    # Vivo
    alive = RewardTermCfg(func=mdp.is_alive, weight=0.1)

    # In piedi
    standing = RewardTermCfg(
        func="isaaclab.envs.mdp.rewards:joint_pos_limits",
        params={
            "asset_cfg": SceneEntityCfg(
                name= "robot",
                joint_names= ["left_hip_pitch_joint","right_hip_pitch_joint"]
            )
        },
        weight=10.0
    )
    
    # Caduto
    fallen = RewardTermCfg(func=mdp.is_terminated, weight=-200.0)

    '''
    # Cammina
    walking = RewardTermCfg(
        func=mdp.joint_vel_l2(
        params={
            asset_cfg= SceneEntityCfg(
                name='robot',
                joint_name='left_knee_joint')
            ),
        }
            
        weight=0.1
    )
    

    # Colpisce un ostacolo
    hit_obstacle = RewardTermCfg(
        func=mdp.undesired_contacts,
        weight=-2.0,
    )

    # Si avvicina all'obiettivo
    approach_goal = RewardTermCfg(
        func="isaaclab.envs.mdp.rewards:goal_distance",
        params={
            "asset_cfg": SceneEntityCfg(name="robot"),
            "target_cfg": SceneEntityCfg(name="goal"),
            "normalize": True,
        },
        weight=-1.0
    )

    # Raggiunge l'obiettivo
    reach_goal = RewardTermCfg(
        func="isaaclab.envs.mdp.rewards:goal_reached",
        params={
            "asset_cfg": SceneEntityCfg(name="robot"),
            "target_cfg": SceneEntityCfg(name="goal"),
            "threshold": 0.3,
        },
        weight=10.0
    )
    '''