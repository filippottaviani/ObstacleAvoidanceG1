import isaaclab.sim as sim_utils
from isaaclab.assets import AssetBaseCfg
from isaaclab.sim.spawners import CylinderCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass 

from sensors import contact_cfg, imu_cfg, rgbd_cfg, lidar_cfg
from robot import g1_cfg

@configclass
class BasicScenarioCfg(InteractiveSceneCfg):

    # robot
    robot = g1_cfg.configuration

    # sensori
    rgbd_camera = rgbd_cfg.configuration
    lidar = lidar_cfg.configuration
    imu = imu_cfg.configuration
    #cont_sensor = contact_cfg.configuration # crea un warning per la mesh

    # ground plane
    ground = AssetBaseCfg(prim_path="/World/defaultGroundPlane",
                          spawn=sim_utils.GroundPlaneCfg())

    # luce
    light = AssetBaseCfg(
        prim_path="/World/Light",
        spawn=sim_utils.DomeLightCfg(intensity=2000.0,
                                      color=(0.75, 0.75, 0.75))
    )

    '''# ostacoli
    obstacle = AssetBaseCfg(prim_path="/World/Obstacle1",
                            spawn=sim_utils.spawn_cylinder(translation=[1.0, 0.0, 1.0],
                                                           prim_path="/World/Obstacle1",
                                                           cfg=CylinderCfg(height=2.0,
                                                                            radius=0.5, # misure necessarie
                                                                            #activate_contact_sensors=True # da attivarte in seguito
                                                                            )
                                                            )
    
    )'''

    # marker dell'obiettivo
    # da implementare

    