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

    # Caduta 
    on_fall = DoneTerm(
        func=mdp_custom.has_fallen_hard, # con la soglia standard 0.3
        time_out=False
    )