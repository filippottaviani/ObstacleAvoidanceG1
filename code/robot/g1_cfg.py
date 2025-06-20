import isaaclab.sim as sim_utils
from isaaclab.actuators import IdealPDActuatorCfg
from isaaclab.assets import ArticulationCfg
from isaaclab.sim.spawners.from_files import UsdFileCfg
from isaaclab.sensors import ImuCfg
from isaaclab.actuators import IdealPDActuatorCfg
from robot import actuators

configuration : ArticulationCfg = ArticulationCfg(prim_path="/World/envs/env_.*/Robot", 
        spawn=UsdFileCfg(
        usd_path="/home/filippo/obstacle_avoidance_g1/code/assets/robot/g1_description/g1_12dof/g1_12dof.usd", 
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=20.0,
            angular_damping=20.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
            ),
        ),

        # articolazioni
        init_state=ArticulationCfg.InitialStateCfg(
            pos=(0.0, 0.0, 0.8),
            joint_pos={
                "left_hip_pitch_joint": 0.0,
                "left_hip_roll_joint": 0.0,
                "left_hip_yaw_joint": 0.0,
                "left_knee_joint": 0.0,
                "left_ankle_pitch_joint": 0.0,
                "left_ankle_roll_joint": 0.0,
                "right_hip_pitch_joint": 0.0,
                "right_hip_roll_joint": 0.0,
                "right_hip_yaw_joint": 0.0,
                "right_knee_joint": 0.0,
                "right_ankle_pitch_joint": 0.0,
                "right_ankle_roll_joint": 0.0
            },
        ),
        
        # attuatori
        actuators = actuators.description,
        soft_joint_pos_limit_factor=0.95
    )




