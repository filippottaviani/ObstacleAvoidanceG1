from stable_baselines3 import SAC
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize
import gymnasium as gym
import torch

from configs.env_config import ObstacleAvoidanceEnvCfg

gym.register(
    id="Isaac-G1ObstacleAvoidance-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={"env_cfg_entry_point": ObstacleAvoidanceEnvCfg},
)


env = DummyVecEnv([lambda: gym.make("Isaac-G1ObstacleAvoidance-v0")])
env = VecNormalize.load("vecnormalize.pkl", env)
env.training = False
env.norm_reward = False

model = SAC.load("sac_obstacle_avoidance", env=env)

obs, _ = env.reset()

while True:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)

    # Check se è finito l'episodio
    if done[0]:
        obs, _ = env.reset()

    env.render()
