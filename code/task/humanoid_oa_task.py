import torch
#from isaaclab. import ManagerBasedTask

class ObstacleAvoidanceTask(ManagerBasedTask):
    def __init__(self, cfg, num_envs, device="cuda"):
        super().__init__(cfg, num_envs, device=device)
        env_spacing = self.cfg.scene.env_spacing

        # Genera target iniziali all'interno di ciascun env
        random_offsets = (torch.rand(num_envs, 2, device=self.device) - 0.5) * env_spacing
        env_positions = self.env_origin[:, :2] + random_offsets
        target_z = torch.full((num_envs,), 0.5, device=self.device)

        self.target_position = torch.cat([env_positions, target_z.unsqueeze(-1)], dim=-1)


    def reset(self, env_ids):
        env_spacing = self.cfg.scene.env_spacing  # recupera env_spacing
        num_resets = len(env_ids)

        # Crea offset casuali all’interno di [-env_spacing/2, env_spacing/2] 
        random_offsets = (torch.rand(num_resets, 2, device=self.device) - 0.5) * env_spacing

        # Calcola le posizioni base della griglia di env
        env_positions = self.env_origin[env_ids, :2]  # coordinate (x,y) dell'env
        env_positions = env_positions + random_offsets

        # Target a z fissa
        target_z = torch.full((num_resets,), 0.5, device=self.device)

        # Combina tutto
        self.target_position[env_ids] = torch.cat(
            [env_positions, target_z.unsqueeze(-1)], dim=-1
        )

