from isaaclab.actuators import IdealPDActuatorCfg

description={"left_hip_pitch_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["left_hip_pitch_joint"]
        ),
        "left_hip_roll_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["left_hip_roll_joint"]
        ),
        "left_hip_yaw_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["left_hip_yaw_joint"]
        ),
        "left_knee_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["left_knee_joint"]
        ),
        "left_ankle_pitch_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["left_ankle_pitch_joint"]
        ),
        "left_ankle_roll_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["left_ankle_roll_joint"]
        ),
        "right_hip_pitch_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["right_hip_pitch_joint"]
        ),
        "right_hip_roll_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["right_hip_roll_joint"]
        ),
        "right_hip_yaw_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["right_hip_yaw_joint"]
        ),
        "right_knee_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["right_knee_joint"]
        ),
        "right_ankle_pitch_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["right_ankle_pitch_joint"]
        ),
        "right_ankle_roll_joint": IdealPDActuatorCfg(
            effort_limit=200.0, stiffness=200.0, damping=20.0,
            joint_names_expr=["right_ankle_roll_joint"]
        )
    }