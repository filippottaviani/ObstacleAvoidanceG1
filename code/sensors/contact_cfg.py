from isaaclab.sensors import ContactSensorCfg


configuration_LH : ContactSensorCfg = ContactSensorCfg(
        prim_path="/World/envs/env_.*/Robot/pelvis",
        update_period=0.0,
        history_length=6,
        debug_vis=True,
        filter_prim_paths_expr=["{ENV_REGEX_NS}/Obstacle1"]
    )

configuration_RH : ContactSensorCfg = ContactSensorCfg(
        prim_path="/World/envs/env_.*/Robot/pelvis",
        update_period=0.0,
        history_length=6,
        debug_vis=True,
        filter_prim_paths_expr=["{ENV_REGEX_NS}/Obstacle1"]
    )