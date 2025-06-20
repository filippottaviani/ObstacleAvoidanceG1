from isaaclab.managers import TerminationTermCfg as DoneTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass
from isaaclab.envs import mdp

@configclass
class TerminationsCfg:

    # Fine episodio
    time_out = DoneTerm(
        func=mdp.time_out, 
        time_out=True
    )

    '''# fuori dallo spazio di lavoro
    cart_out_of_bounds = DoneTerm(
        func=mdp.joint_pos_out_of_manual_limit,
        params={"g1_cfg": SceneEntityCfg("robot", joint_names=[ "left_knee_joint"]), "bounds": (-3.0, 3.0)},
    )'''

    # raggiunge l'obiettivo
    # da implementare

    # colpisce l'ostacolo
    # da implementare