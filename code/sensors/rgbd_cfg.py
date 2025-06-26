from isaaclab.sensors import CameraCfg
import isaaclab.sim as sim_utils


# disaccoppiate per le carateristiche diverse diverse 
configuration_rgb : CameraCfg = CameraCfg( 
    prim_path="{ENV_REGEX_NS}/Robot/pelvis/torso_link/d435_link/realsense_rgb",
    update_period=0.1,
    height=192, # la risoluzione è 10x ma riempie il buffer
    width=108, 
    data_types=["rgb"], 
    spawn=sim_utils.PinholeCameraCfg(
        horizontal_aperture=3.126, 
        vertical_aperture=1.807,
    )
)

configuration_depth : CameraCfg = CameraCfg( 
    prim_path="{ENV_REGEX_NS}/Robot/pelvis/torso_link/d435_link/realsense_depth",
    update_period=0.1,
    height=128, # la risoluzione è 10x ma riempie il buffer
    width=72, 
    data_types=["depth"], 
    spawn=sim_utils.PinholeCameraCfg(
        horizontal_aperture=3.896, 
        vertical_aperture=2.453,
    )
)
