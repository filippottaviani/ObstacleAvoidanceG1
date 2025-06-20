from isaaclab.managers import TerminationTermCfg as DoneTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass
from managers.mdp import mdp_custom
from isaaclab.envs import mdp

@configclass
class TerminationsCfg:

    # Fine episodio
    time_out = DoneTerm(
        func=mdp.time_out, 
        time_out=True
    )

    # caduta
    reset_on_fall = DoneTerm(
        func=mdp_custom.fallen_reset
    )

    '''# fuori dallo spazio di lavoro
    cart_out_of_bounds = DoneTerm(
        func=mdp.joint_pos_out_of_manual_limit,
        params={"g1_cfg": SceneEntityCfg("robot", joint_names=[ "left_knee_joint"]), "bounds": (-3.0, 3.0)},
    )'''

    '''# colpisce l'ostacolo
    contact = DoneTerm(
        func=mdp.illegal_contact
        # da parametrizzare
    )'''

    # raggiunge l'obiettivo
    # da implementare

    