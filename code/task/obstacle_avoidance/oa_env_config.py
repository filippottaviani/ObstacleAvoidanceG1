from managers.obstacle_avoidance.event_manager_cfg import EventsCfg
from managers.obstacle_avoidance.action_manager_cfg import ActionsCfg
from managers.obstacle_avoidance.observation_manager_cfg import ObservationsCfg
from managers.obstacle_avoidance.reward_manager_cfg import RewardsCfg
from managers.obstacle_avoidance.termination_manager_cfg import TerminationsCfg
from managers.obstacle_avoidance.curriculum_manager_cfg import CurriculumCfg
from managers.obstacle_avoidance.command_manager_cfg import CommandsCfg
from scenes.basic_scenario import BasicScenarioCfg

from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.utils import configclass

@configclass
class ObstacleAvoidanceEnvCfg(ManagerBasedRLEnvCfg):
    env_spacing = 5

    # configurazione dell'environment
    scene : BasicScenarioCfg = BasicScenarioCfg(env_spacing)
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
        self.decimation = 2
        self.episode_length_s = 20

        # Impostazioni di simulazione
        self.sim.dt = 0.005  # step
        self.sim.render_interval = self.decimation