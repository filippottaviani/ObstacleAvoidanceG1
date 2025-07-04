from managers.standing.event_manager_cfg import EventsCfg
from managers.standing.action_manager_cfg import ActionsCfg
from managers.standing.observation_manager_cfg import ObservationsCfg
from managers.standing.reward_manager_cfg import RewardsCfg
from managers.standing.termination_manager_cfg import TerminationsCfg
from managers.standing.curriculum_manager_cfg import CurriculumCfg
from managers.standing.command_manager_cfg import CommandsCfg
from scenes.empty_scenario import EmptyScenario

from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.utils import configclass


@configclass
class StandingEnvCfg(ManagerBasedRLEnvCfg):
    env_spacing = 5

    # configurazione dell'environment
    scene : EmptyScenario = EmptyScenario(env_spacing)
    observations : ObservationsCfg = ObservationsCfg()
    actions : ActionsCfg = ActionsCfg()
    events : EventsCfg = EventsCfg()
    rewards : RewardsCfg = RewardsCfg()
    terminations : TerminationsCfg = TerminationsCfg()
    commands : CommandsCfg = CommandsCfg()
    curriculum: CurriculumCfg = CurriculumCfg()


    def __post_init__(self) -> None:
        # Impostazioni visive
        self.viewer.eye = [15, 0.0, 6.0]
        self.viewer.lookat = [0.0, 0.0, 1.0]

        # Impostazioni dell'episodio
        self.decimation = 4
        self.episode_length_s = 10

        # Impostazioni di simulazione
        self.sim.dt = 0.005  # step
        self.sim.render_interval = self.decimation