from isaaclab.sensors import ImuCfg
from isaaclab.sensors import OffsetCfg


configuration : ImuCfg = ImuCfg(
    prim_path="{ENV_REGEX_NS}/Robot/pelvis",
    update_period=0.01
)