from isaaclab.app import AppLauncher
import argparse

parser = argparse.ArgumentParser(description="Test del modello per evitamento ostacoli di un robot umanoide.")
parser.add_argument("--num_episodes", type=int, default=10, help="Numero di episodi da simulare.")
parser.add_argument("--task", type=str, default="Isaac-G1Locomotion", help="Nome del task.")
parser.add_argument("--video" , action="store_true", default=False, help="Registrazione video durante l'addestramento.")
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

import gymnasium as gym
import os, time, torch
import numpy as np
from datetime import datetime
from pathlib import Path

from task.task_register import * 


def main():
    # Configurazione
    task = args_cli.task
    env_cfg = load_cfg_from_registry(task, "env_cfg_entry_point")
    agent_cfg = load_cfg_from_registry(task, "sb3_cfg_entry_point")
    
    # Percorso del modello salvato
    #model_path = os.path.expanduser("~/obstacle_avoidance_g1/code/checkpoints/models/Isaac-G1ObstacleAvoidance/2025-07-02_11-33-41.zip")
    root_path = os.path.expanduser("~/obstacle_avoidance_g1/code")
    mod_root_path =os.path.join(root_path, "checkpoints/models", task)
    model_path = os.path.join(mod_root_path,"2025-07-03_11-28-13.zip") 

    # Configurazione della simualazione
    env_cfg.scene.num_envs = 1
    env_cfg.sim.device = "cuda:0"
    env_cfg.sim.dt = 0.02
    env_cfg.sim.use_gpu_pipeline = True

    # Percorsi
    root_path = Path.home() / "obstacle_avoidance_g1"/ "code" / "checkpoints"
    log_root_path = os.path.join("logs", task)
    log_root_path = os.path.abspath(log_root_path)
    
    # impostazione video logging
    video_root_path = os.path.join(root_path,"videos", task)
    run_info = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    video_dir = os.path.join(video_root_path, run_info)

    # Post-process delle configurazioni
    agent_cfg = process_sb3_cfg(agent_cfg)

    # Creazione dell'ambiente
    env = gym.make(
        task,
        cfg=env_cfg, 
        render_mode="rgb_array" if args_cli.video else None
    )

    # Wrap per la registrazione video
    if args_cli.video:
        video_kwargs = {
            "video_folder": os.path.join(video_dir, "test"),
            "step_trigger": lambda step: step % args_cli.video_interval == 0,
            "video_length": args_cli.video_length,
            "disable_logger": True,
        }
        print("[INFO] Recording videos during training.")
        print_dict(video_kwargs, nesting=4)
        env = gym.wrappers.RecordVideo(env, **video_kwargs)

    # Wrap per stable baselines
    env = Sb3VecEnvWrapper(env)

    # Caricamento delle statistiche di normalizzazione
    vecnorm_path = os.path.join(root_path,"normalization", "vecnormalize.pkl")
    if os.path.exists(vecnorm_path):
        env = VecNormalize.load(vecnorm_path, env)
        env.training = False
        env.norm_reward = False
    elif "normalize_input" in agent_cfg:
        env = VecNormalize(
            env,
            training=False,
            norm_obs="normalize_input" in agent_cfg and agent_cfg.pop("normalize_input"),
            clip_obs="clip_obs" in agent_cfg and agent_cfg.pop("clip_obs"),
        )
    else:
        print(f"[ATTENZIONE] File di normalizzazione non trovato: {vecnorm_path}")

    # Caricamento del modello
    print(f"Caricamento dell'agente da {model_path}")
    model = SAC.load(
        model_path, 
        env=env, 
        verbose=1, 
        print_system_info=True
    )

    # Valutazione del modello
    # Il wrapper SB3 per Isaaclab non supporta direttamente evaluate_policy
    obs = env.reset()
    timestep = 0
    start_time = time.time()

    while simulation_app.is_running():
        
        with torch.inference_mode():
            actions, _ = model.predict(obs, deterministic=True) # Step dell'agente
            obs, reward, done, info = env.step(actions) # Step dell'ambiente 
            if done[0]:
                print(f"[INFO] Episodio terminato con reward: {reward[0]:.2f}")
                obs = env.reset()
        if args_cli.video:
            timestep += 1
            if timestep == args_cli.video_length:
                break

    duration = time.time() - start_time
    h, r = divmod(duration, 3600)
    m, s = divmod(r, 60)
    print(f"Test per {task} terminato in {int(h)} ore, {int(m)} minuti e {int(s)} secondi.")


if __name__ == "__main__":
    main()
    if simulation_app is not None:
        simulation_app.close()
