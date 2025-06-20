from isaaclab.sensors import ContactSensorCfg


configuration : ContactSensorCfg = ContactSensorCfg(
        prim_path="/World/envs/env_.*/Robot/right_ankle_roll_link",
        update_period=0.0,
        history_length=6,
        debug_vis=True,
    )