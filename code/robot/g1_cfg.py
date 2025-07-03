# Configurazione utilizzata in:
# https://github.com/isaac-sim/IsaacLab/blob/main/source/isaaclab_assets/isaaclab_assets/robots/unitree.py#L273

import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg
from isaaclab.sim.spawners.from_files import UsdFileCfg
from robot import actuators

configuration : ArticulationCfg = ArticulationCfg(
    prim_path="/World/envs/env_.*/Robot", 
    spawn=UsdFileCfg(
        usd_path="/home/filippo/obstacle_avoidance_g1/code/assets/robot/g1_description/g1_12dof/g1_12dof.usd", 
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=4,
        ),
    ),

    # articolazioni
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.8),
        joint_pos={
            ".*_hip_pitch_joint": -0.2,
            ".*_hip_roll_joint": 0.0,
            ".*_hip_yaw_joint": 0.0,
            ".*_knee_joint": 0.42,
            ".*_ankle_pitch_joint": -0.23,
            ".*_ankle_roll_joint": 0.0
        },
        joint_vel={".*": 0.0},
    ),
    
    # attuatori
    actuators = actuators.description,
    soft_joint_pos_limit_factor=0.9
)
