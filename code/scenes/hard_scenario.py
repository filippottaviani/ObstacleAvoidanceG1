import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg, AssetBaseCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass 

from sensors import contact_cfg, imu_cfg, rgbd_cfg, lidar_cfg
from robot import g1_cfg
    

@configclass
class HardScenarioCfg(InteractiveSceneCfg):
    # robot
    robot = g1_cfg.configuration

    # sensori
    rgbd_camera = rgbd_cfg.configuration
    lidar = lidar_cfg.configuration
    imu = imu_cfg.configuration
    cont_sensor_LH = contact_cfg.configuration_LH
    cont_sensor_RH = contact_cfg.configuration_RH

    # ground plane
    ground = AssetBaseCfg(prim_path="/World/defaultGroundPlane",
                          spawn=sim_utils.GroundPlaneCfg())

    # luce
    light = AssetBaseCfg(
        prim_path="/World/Light",
        spawn=sim_utils.DomeLightCfg(intensity=2000.0,
                                      color=(0.75, 0.75, 0.75))
    )

    # Ostacoli
    # da implementare s