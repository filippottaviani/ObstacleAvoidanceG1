from isaaclab.utils import configclass
from isaaclab.envs.mdp import JointEffortActionCfg, JointVelocityActionCfg, JointPositionActionCfg
import torch

@configclass
class ActionsCfg:

    '''joint_efforts = JointEffortActionCfg(
        asset_name="robot", 
        joint_names=[".*"],
        scale= 0.5,
        use_default_offset=True
    )'''

    '''joint_efforts = JointVelocityActionCfg(
        asset_name="robot", 
        joint_names=[".*"],
        scale= 0.5,
        use_default_offset=True
    )'''

    joint_pos = JointPositionActionCfg(
        asset_name="robot", 
        joint_names=[".*"], 
        scale=0.5, 
        use_default_offset=True
    )

