import isaaclab.sim as sim_utils
from isaaclab.assets import AssetBaseCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass 
from isaaclab.terrains import TerrainImporterCfg
from isaaclab.terrains.config.rough import ROUGH_TERRAINS_CFG
from isaaclab.utils.assets import ISAACLAB_NUCLEUS_DIR

from sensors import contact_cfg, imu_cfg, rgbd_cfg, lidar_cfg
from robot import g1_cfg
    

@configclass
class HardScenarioCfg(InteractiveSceneCfg):
    # robot
    robot = g1_cfg.configuration

    # sensori
    rgb_camera = rgbd_cfg.configuration_rgb
    depth_camera = rgbd_cfg.configuration_depth
    lidar = lidar_cfg.configuration
    imu = imu_cfg.configuration
    cont_sensor_LH = contact_cfg.configuration_LH
    cont_sensor_RH = contact_cfg.configuration_RH

    # Terreno con asperità
    terrain = TerrainImporterCfg(
        prim_path="/World/ground",
        terrain_type="generator",
        terrain_generator=ROUGH_TERRAINS_CFG,
        max_init_terrain_level=5,
        collision_group=-1,
        physics_material=sim_utils.RigidBodyMaterialCfg(
            friction_combine_mode="multiply",
            restitution_combine_mode="multiply",
            static_friction=1.0,
            dynamic_friction=1.0,
        ),
        visual_material=sim_utils.MdlFileCfg(
            mdl_path=f"{ISAACLAB_NUCLEUS_DIR}/Materials/TilesMarbleSpiderWhiteBrickBondHoned/TilesMarbleSpiderWhiteBrickBondHoned.mdl",
            project_uvw=True,
            texture_scale=(0.25, 0.25),
        ),
        debug_vis=False,
    )

    # luce
    light = AssetBaseCfg(
        prim_path="/World/Light",
        spawn=sim_utils.DomeLightCfg(
            intensity=2000.0,
            color=(0.75, 0.75, 0.75)
        )
    )

    # Ostacoli
    # da implementare s