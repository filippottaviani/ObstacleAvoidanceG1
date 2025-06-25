from isaaclab.utils import configclass
from isaaclab.envs.mdp import JointEffortActionCfg

@configclass
class ActionsCfg:

    joint_efforts = JointEffortActionCfg(
        asset_name="robot", 
        joint_names=[
            "left_hip_pitch_joint",
            "left_hip_roll_joint",
            "left_hip_yaw_joint",
            "left_knee_joint",
            "left_ankle_pitch_joint",
            "left_ankle_roll_joint",
            "right_hip_pitch_joint",
            "right_hip_roll_joint",
            "right_hip_yaw_joint",
            "right_knee_joint",
            "right_ankle_pitch_joint",
            "right_ankle_roll_joint"
        ],
        scale= 1.0
    )