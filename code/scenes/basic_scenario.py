import isaaclab.sim as sim_utils
from isaaclab.assets import AssetBaseCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass 

from sensors import contact_cfg, imu_cfg, rgbd_cfg, lidar_cfg
from robot import g1_cfg


@configclass
class BasicScenarioCfg(InteractiveSceneCfg):

    # Robot
    robot = g1_cfg.configuration

    # Sensori
    '''rgb_camera = rgbd_cfg.configuration_rgb
    depth_camera = rgbd_cfg.configuration_depth
    lidar = lidar_cfg.configuration'''
    imu = imu_cfg.configuration
    contact_sensor_feet = contact_cfg.configuration_feet
    #cont_sensor_LH = contact_cfg.configuration_LH
    #cont_sensor_RH = contact_cfg.configuration_RH

    # Ground plane
    ground = AssetBaseCfg(
        prim_path="/World/defaultGroundPlane",
        spawn=sim_utils.GroundPlaneCfg()
    )

    # Luce
    light = AssetBaseCfg(
        prim_path="/World/Light",
        spawn=sim_utils.DomeLightCfg(
            intensity=2000.0,
            color=(0.75, 0.75, 0.75)
        )
    )

    # Ostacoli
    obstacle1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/Obstacle1",
        spawn= sim_utils.CylinderCfg(
            radius=0.2,
            height=2,
            rigid_props=sim_utils.RigidBodyPropertiesCfg(
                disable_gravity=False
            ),
            mass_props=sim_utils.MassPropertiesCfg(mass=100.0),
            collision_props=sim_utils.CollisionPropertiesCfg(
                collision_enabled=True
            ),
            physics_material=sim_utils.RigidBodyMaterialCfg(static_friction=1.0),
            activate_contact_sensors=True
        ),
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.0, 0.0, 1.0),
        )
    )

    obstacle2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/Obstacle2",
        spawn= sim_utils.CylinderCfg(
            radius=0.2,
            height=2,
            rigid_props=sim_utils.RigidBodyPropertiesCfg(
                disable_gravity=False
            ),
            mass_props=sim_utils.MassPropertiesCfg(mass=100.0),
            collision_props=sim_utils.CollisionPropertiesCfg(
                collision_enabled=True
            ),
            physics_material=sim_utils.RigidBodyMaterialCfg(static_friction=1.0),
            activate_contact_sensors=True
        ),
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.0, 0.0, -0.5),
        )
    )