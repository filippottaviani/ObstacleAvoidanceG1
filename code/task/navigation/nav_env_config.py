from managers.navigation.event_manager_cfg import EventsCfg
from managers.navigation.action_manager_cfg import ActionsCfg
from managers.navigation.observation_manager_cfg import ObservationsCfg
from managers.navigation.reward_manager_cfg import RewardsCfg
from managers.navigation.termination_manager_cfg import TerminationsCfg
from managers.navigation.curriculum_manager_cfg import CurriculumCfg
from managers.navigation.command_manager_cfg import CommandsCfg
from scenes.empty_scenario import EmptyScenario

from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.utils import configclass


@configclass
class NavigationEnvCfg(ManagerBasedRLEnvCfg):
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
        self.viewer.lookat = [0.0, 0.0, 3.0]

        # Impostazioni dell'episodio
        self.decimation = 4
        self.episode_length_s = 30

        # Impostazioni di simulazione
        self.sim.dt = 0.005  # step
        self.sim.render_interval = self.decimation