import argparse

from isaaclab.app import AppLauncher


# add argparse arguments
parser = argparse.ArgumentParser(description="Addestramento per evitamento ostacoli di un robot umanoide.")
parser.add_argument("--video", default=False, help="Registrazione video durante l'addestramento.")
parser.add_argument("--video_length", type=int, default=200, help="Lunghezza delle registrazioni video (in steps).")
parser.add_argument("--video_interval", type=int, default=200000, help="Intervallo tra registrazioni video (in steps).")
parser.add_argument("--num_envs", type=int, default=1, help="Numero di ambienti da simulare.")
parser.add_argument("--task", type=str, default=None, help="Nome del task.")
parser.add_argument("--seed", type=int, default=None, help="Seed utilizzato.")
parser.add_argument("--max_iterations", type=int, default=100000, help="Iterazione per ogni ambiente.")

# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)
# parse the arguments
args_cli = parser.parse_args()
# always enable cameras to record video
if args_cli.video:
    args_cli.enable_cameras = True

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app


######################### TRAINER #########################


from isaaclab_rl.sb3 import Sb3VecEnvWrapper, process_sb3_cfg
from isaaclab.utils.dict import print_dict
from isaaclab_tasks.utils import load_cfg_from_registry
from isaaclab.utils.io import dump_pickle, dump_yaml

import gymnasium as gym
import numpy as np
import os, time
from datetime import datetime
from pathlib import Path

from stable_baselines3 import SAC
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.logger import configure
from stable_baselines3.common.vec_env import VecNormalize

from configs.env_config import ObstacleAvoidanceEnvCfg
from task.task_register import * 


def main():
    # Configurazione
    task = "Isaac-G1ObstacleAvoidance"
    env_cfg = ObstacleAvoidanceEnvCfg()
    agent_cfg = load_cfg_from_registry(task, "sb3_cfg_entry_point")

    # Numero di ambienti
    env_cfg.scene.num_envs = args_cli.num_envs if args_cli.num_envs is not None else env_cfg.scene.num_envs

    # override configuration with command line arguments
    if args_cli.seed is not None:
        agent_cfg["seed"] = args_cli.seed

    # max iterations for training
    if args_cli.max_iterations:
        agent_cfg["n_timesteps"] = args_cli.max_iterations * env_cfg.scene.num_envs

    # Impostazioni log
    root_path = Path.home() / "obstacle_avoidance_g1"/ "code" / "checkpoints"
    run_info = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_root_path = os.path.join(root_path,"logs", task)
    log_dir = os.path.join(log_root_path, run_info)
    print(f"[INFO] Logging experiment in directory: {log_root_path}")

    # Scrittura della configurazione nella cartella log
    dump_yaml(os.path.join(log_dir, "params", "env.yaml"), env_cfg)
    dump_yaml(os.path.join(log_dir, "params", "agent.yaml"), agent_cfg)
    dump_pickle(os.path.join(log_dir, "params", "env.pkl"), env_cfg)
    dump_pickle(os.path.join(log_dir, "params", "agent.pkl"), agent_cfg)

    # Post-process delle configurazioni
    agent_cfg = process_sb3_cfg(agent_cfg)
    policy_arch = agent_cfg.pop("policy")
    n_timesteps = agent_cfg.pop("n_timesteps")

    # Creazione env Isaac
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

    env = VecNormalize(
        env,
        training=True,
        norm_obs="normalize_input" in agent_cfg and agent_cfg.pop("normalize_input"),
        norm_reward="normalize_value" in agent_cfg and agent_cfg.pop("normalize_value"),
        clip_obs="clip_obs" in agent_cfg and agent_cfg.pop("clip_obs"),
        gamma=agent_cfg["gamma"],
        clip_reward=np.inf
    )

    # Creazione dell'agente
    agent = SAC(
        policy_arch, 
        env, verbose=1, 
        **agent_cfg
    )
    new_logger = configure(log_dir, ["stdout", "tensorboard"])
    agent.set_logger(new_logger)

    # Callback dell'agente 
    checkpoint_callback = CheckpointCallback(save_freq=10000, save_path=log_dir, name_prefix="model", verbose=2)

    # Debug spazi
    #print("Spazio di osservazione: ", env.observation_space)
    #print("Spazio d'azione: ",env.action_space)

    # Addestramento
    start_time = time.time()
    agent.learn(total_timesteps=n_timesteps, callback=checkpoint_callback)

    # Segnalazione fine dell'addestramento
    duration = time.time() - start_time
    h, r = divmod(duration, 3600)
    m, s = divmod(r, 60)
    print(f"Addestramento terminato in {int(h)} ore, {int(m)} minuti e {int(s)} secondi.")

    # Salvataggio del modello
    mod_root_path =os.path.join(root_path,"models", task)
    mod_dir = os.path.join(mod_root_path, run_info)
    agent.save(mod_dir, "model")

    # Chiusura env
    env.close()


if __name__ == "__main__":
    main()
    simulation_app.close()