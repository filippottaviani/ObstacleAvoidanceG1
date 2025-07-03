import isaaclab.sim as sim_utils
from isaaclab.assets import AssetBaseCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass 

from sensors import contact_cfg, imu_cfg, rgbd_cfg, lidar_cfg
from robot import g1_cfg as g1_custom
from robot import g1_cfg_alt as g1


#env_spacing: float = 10.0  # Spaziatura dell'ambiente

@configclass
class EmptyScenario(InteractiveSceneCfg):

    # robot
    robot = g1_custom.configuration # carica il modello standard di IsaacLab

    # sensori
    #rgb_camera = rgbd_cfg.configuration_rgb
    #depth_camera = rgbd_cfg.configuration_depth
    #lidar = lidar_cfg.configuration
    imu = imu_cfg.configuration
    contact_sensor_feet = contact_cfg.configuration_feet
    #cont_sensor_LH = contact_cfg.configuration_LH
    #cont_sensor_RH = contact_cfg.configuration_RH

    # ground plane
    ground = AssetBaseCfg(
        prim_path="/World/defaultGroundPlane",
        spawn=sim_utils.GroundPlaneCfg()
    )

    # luce
    light = AssetBaseCfg(
        prim_path="/World/Light",
        spawn=sim_utils.DomeLightCfg(
            intensity=2000.0,
            color=(0.75, 0.75, 0.75)
        )
    )
