from isaaclab.actuators import ImplicitActuatorCfg

description={
    "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_hip_yaw_joint",
                ".*_hip_roll_joint",
                ".*_hip_pitch_joint",
                ".*_knee_joint"
            ],
            effort_limit=300,
            velocity_limit=100.0,
            stiffness={
                ".*_hip_yaw_joint": 150.0,
                ".*_hip_roll_joint": 150.0,
                ".*_hip_pitch_joint": 200.0,
                ".*_knee_joint": 200.0
            },
            damping={
                ".*_hip_yaw_joint": 5.0,
                ".*_hip_roll_joint": 5.0,
                ".*_hip_pitch_joint": 5.0,
                ".*_knee_joint": 5.0
            },
            armature={
                ".*_hip_.*": 0.01,
                ".*_knee_joint": 0.01
            },
        ),
        "feet": ImplicitActuatorCfg(
            effort_limit=20,
            joint_names_expr=[
                ".*_ankle_pitch_joint", 
                ".*_ankle_roll_joint"
            ],
            stiffness=100.0,
            damping=5.0,
            armature=0.01,
        )
}