from managers.locomotion.event_manager_cfg import EventsCfg
from managers.locomotion.action_manager_cfg import ActionsCfg
from managers.locomotion.observation_manager_cfg import ObservationsCfg
from managers.locomotion.reward_manager_cfg import RewardsCfg
from managers.locomotion.termination_manager_cfg import TerminationsCfg
from managers.locomotion.curriculum_manager_cfg import CurriculumCfg
from managers.locomotion.command_manager_cfg import CommandsCfg
from scenes.empty_scenario import EmptyScenario

from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.utils import configclass


@configclass
class LocomotionEnvCfg(ManagerBasedRLEnvCfg):

    # configurazione dell'environment
    scene : EmptyScenario = EmptyScenario(env_spacing=5)
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
        self.decimation = 2
        self.episode_length_s = 10

        # Impostazioni di simulazione
        self.sim.dt = 0.005  # step
        self.sim.render_interval = self.decimation