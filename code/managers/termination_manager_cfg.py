from isaaclab.managers import TerminationTermCfg as DoneTerm
from isaaclab.managers import SceneEntityCfg
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

    # Caduta del robot
    reset_on_fall = DoneTerm(
        func=mdp_custom.has_fallen
    )

    # Fuori dallo spazio di lavoro
    out_of_bounds = DoneTerm(
        func=mdp_custom.out_of_manual_bound,
        params={
            "max_dist": 5,  # distanza dall'origine 
            "ref_link": "pelvis"  # link di riferimento 
        }
    )

    '''# Colpisce l'ostacolo
    hit_obstacle = DoneTerm(
        func=mdp.undesired_contacts,
        params={
            "threshold": 0.1,  # soglia di contatto
            "sensor_cfg": SceneEntityCfg(
                name="cont_sensor_LH"  # nome del sensore dell'ostacolo
            ),
        },
    )'''

    # raggiunge l'obiettivo
    reach_goal = DoneTerm(
        func=mdp_custom.target_reached
    )

    