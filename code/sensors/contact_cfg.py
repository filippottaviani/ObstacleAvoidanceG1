from isaaclab.sensors import ContactSensorCfg


# Sensore di contatto mano sinistra
configuration_LH : ContactSensorCfg = ContactSensorCfg(
    prim_path="/World/envs/env_.*/Robot/pelvis",
    update_period=0.0,
    history_length=6,
    debug_vis=True,
    filter_prim_paths_expr=["{ENV_REGEX_NS}/"]
)

# Sensore di contatto mano destra
configuration_RH : ContactSensorCfg = ContactSensorCfg(
    prim_path="/World/envs/env_.*/Robot/pelvis",
    update_period=0.0,
    history_length=6,
    debug_vis=True,
    filter_prim_paths_expr=["{ENV_REGEX_NS}/"]
)

# Sensore di contatto piedi
configuration_feet = ContactSensorCfg(
    prim_path="{ENV_REGEX_NS}/Robot/.*", 
    history_length=3, 
    track_air_time=True
)