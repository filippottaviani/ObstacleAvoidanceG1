from isaaclab.utils import configclass
from isaaclab.envs import mdp


@configclass
class CommandsCfg:
    null = mdp.NullCommandCfg()