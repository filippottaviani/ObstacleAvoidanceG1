from isaaclab.app import AppLauncher
import argparse

parser = argparse.ArgumentParser(description="Test del modello per evitamento ostacoli di un robot umanoide.")
parser.add_argument("--num_envs", type=int, default=1, help="Numero di ambienti da simulare.")
parser.add_argument("--num_episodes", type=int, default=10, help="Numero di episodi da simulare.")
parser.add_argument("--video", default=False, help="Registrazione video durante l'addestramento.")
parser.add_argument("--video_length", type=int, default=200, help="Lunghezza delle registrazioni video (in steps).")
parser.add_argument("--video_interval", type=int, default=2000, help="Intervallo tra registrazioni video (in steps).")

AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args()

app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app


######################### TESTER #########################


from isaaclab.utils.dict import print_dict
from isaaclab_rl.sb3 import Sb3VecEnvWrapper, process_sb3_cfg
from isaaclab_tasks.utils import load_cfg_from_registry

from stable_baselines3 import SAC
from stable_baselines3.common.vec_env import VecNormalize

from torch.utils.tensorboard.writer import SummaryWriter
import gymnasium as gym
import os, time
import numpy as np
from datetime import datetime
from pathlib import Path

from configs.env_config import ObstacleAvoidanceEnvCfg
from task.task_register import * 


# Percorso del modello salvato
model_path = os.path.expanduser("~/obstacle_avoidance_g1/code/checkpoints/models/Isaac-G1ObstacleAvoidance/sac_obstacle_avoidance")

# Configurazione dell'ambiente
task = "Isaac-G1ObstacleAvoidance"
env_cfg = ObstacleAvoidanceEnvCfg()
agent_cfg = load_cfg_from_registry(task, "sb3_cfg_entry_point")

# impostazione video logging
root_path = Path.home() / "obstacle_avoidance_g1"/ "code" / "checkpoints"
run_info = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_root_path = os.path.join(root_path,"videos", task)
log_dir = os.path.join(log_root_path, run_info)

# Numero di ambienti e episodi
env_cfg.scene.num_envs = args_cli.num_envs
num_episodes = args_cli.num_episodes 

 # Post-process delle configurazioni
agent_cfg = process_sb3_cfg(agent_cfg)
policy_arch = agent_cfg.pop("policy")

# Creazione dell'ambiente
env = gym.make(
    task,
    cfg=env_cfg, 
    render_mode="rgb_array" if args_cli.video else None
)

# Wrap per la registrazione video
if args_cli.video:
    video_kwargs = {
        "video_folder": os.path.join(log_dir, "videos"),
        "step_trigger": lambda step: step % args_cli.video_interval == 0,
        "video_length": args_cli.video_length,
        "disable_logger": True,
    }
    print("[INFO] Recording videos during training.")
    print_dict(video_kwargs, nesting=4)
    env = gym.wrappers.RecordVideo(env, **video_kwargs)

# Wrap per stable baselines
env = Sb3VecEnvWrapper(env)

# Normalizzazioni
env = VecNormalize(
    env,
    training=True,
    norm_obs="normalize_input" in agent_cfg and agent_cfg.pop("normalize_input"),
    norm_reward="normalize_value" in agent_cfg and agent_cfg.pop("normalize_value"),
    clip_obs="clip_obs" in agent_cfg and agent_cfg.pop("clip_obs"),
    gamma= "gamma" in agent_cfg and agent_cfg.pop("gamma"),
    clip_reward=np.inf,
)

# Caricamento del modello
model = SAC.load(
    model_path, 
    env=env, 
    verbose=1, 
    **agent_cfg
)

# Valutazione del modello
# Il wrapper SB3 per Isaaclab non supporta direttamente evaluate_policy
obs = env.reset()
episode_rewards = []

start_time = time.time()
for ep in range(num_episodes):
    done = False
    total_reward = 0
    obs = env.reset()

    while not done:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        total_reward += reward
        
        env.render() # Per vedere la simulazione
    episode_rewards.append(total_reward)

duration = time.time() - start_time
h, r = divmod(duration, 3600)
m, s = divmod(r, 60)
print(f"Test terminato in {int(h)} ore, {int(m)} minuti e {int(s)} secondi.")
print(f"Ricompensa media: {np.mean(episode_rewards)}")

simulation_app.close()