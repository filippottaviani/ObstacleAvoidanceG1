from isaaclab.sensors import RayCasterCfg, patterns
 
 
configuration : RayCasterCfg = RayCasterCfg(
        prim_path="{ENV_REGEX_NS}/Robot/pelvis/torso_link/mid360_link",
        mesh_prim_paths=["/World"], # per ora rileva solo il terreno 
        update_period=0.1,
        attach_yaw_only=False,
        pattern_cfg=patterns.LidarPatternCfg(
            channels=40,
            vertical_fov_range=[7.0, -52.0], 
            horizontal_fov_range=[-180.0, 180.0], 
            horizontal_res=0.15
        )
    )