import os
import gymnasium as gym
from configs.env_config import ObstacleAvoidanceEnvCfg

# Ottieni il percorso assoluto del file di configurazione
task_config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "agent_config.yaml")

gym.register(
    id="Isaac-G1ObstacleAvoidance",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": ObstacleAvoidanceEnvCfg,
        "sb3_cfg_entry_point": task_config_path
    }
)
