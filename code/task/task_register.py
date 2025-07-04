import os
import gymnasium as gym
from task.obstacle_avoidance.oa_env_config import ObstacleAvoidanceEnvCfg
from task.navigation.nav_env_config import NavigationEnvCfg
from task.locomotion.loc_env_config import LocomotionEnvCfg
from task.standing.stan_env_config import StandingEnvCfg

# Ottieni il percorso assoluto del file di configurazione
agent_config_path = os.path.join(os.path.dirname(__file__), "..", "agent", "config.yaml")

gym.register(
    id="Isaac-G1Standing",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": StandingEnvCfg,
        "sb3_cfg_entry_point": agent_config_path
    }
)

gym.register(
    id="Isaac-G1Locomotion",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": LocomotionEnvCfg,
        "sb3_cfg_entry_point": agent_config_path
    }
)

gym.register(
    id="Isaac-G1Navigation",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": NavigationEnvCfg,
        "sb3_cfg_entry_point": agent_config_path
    }
)

gym.register(
    id="Isaac-G1ObstacleAvoidance",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": ObstacleAvoidanceEnvCfg,
        "sb3_cfg_entry_point": agent_config_path
    }
)
