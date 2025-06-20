from isaaclab.sensors import CameraCfg
import isaaclab.sim as sim_utils


configuration : CameraCfg = CameraCfg( # uso Tiled per efficienza
    prim_path="{ENV_REGEX_NS}/Robot/pelvis/torso_link/d435_link/Realsense",
    #offset=TiledCameraCfg.OffsetCfg(pos=(0.0, 0.0, 0.0), rot=(-0.23538, 0.76070, 0.38126, 0.46963), convention="world"), # in quaternioni
    update_period=0.1,
    height=192,
    width=108, # la risoluzione è 10x ma non è fattibile 
    data_types=["rgb","depth"], 
    spawn=sim_utils.PinholeCameraCfg(
        focal_length=35.0, 
        horizontal_aperture=3.126, 
        vertical_aperture=1.807,
    )
)
