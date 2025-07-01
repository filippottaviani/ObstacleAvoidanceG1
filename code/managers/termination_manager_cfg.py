from isaaclab.managers import TerminationTermCfg as DoneTerm
from isaaclab.utils import configclass
from managers.mdp import mdp_rew_custom as mdp_custom

from isaaclab.envs import mdp

@configclass
class TerminationsCfg:

    # Fine episodio
    time_out = DoneTerm(
        func=mdp.time_out, 
        time_out=True
    )

