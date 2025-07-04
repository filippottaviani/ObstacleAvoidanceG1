import isaaclab.sim as sim_utils
from isaaclab.assets import AssetBaseCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.utils import configclass 

from sensors import contact_cfg, imu_cfg
from robot import g1_cfg as g1_custom
from robot import g1_cfg_alt as g1


@configclass
class EmptyScenario(InteractiveSceneCfg):

    # Robot
    robot = g1_custom.configuration # carica il modello standard di IsaacLab

    # Sensori
    imu = imu_cfg.configuration
    contact_sensor_feet = contact_cfg.configuration_feet

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
