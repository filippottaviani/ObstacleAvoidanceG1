import torch
import torch.nn as nn
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor


class RGBDCNNFeatureExtractor(BaseFeaturesExtractor):
    def __init__(self, obs_space, features_dim: int = 256):
        super().__init__(obs_space, features_dim)

        # Dimensioni immagini
        rgb_shape = obs_space["rgb_image"].shape  # (1, H, W, 3)
        depth_shape = obs_space["depth_image"].shape  # (1, H, W, 1)

        # Converti da (B, 1, H, W, C) a (B, C, H, W)
        rgb_chan, rgb_h, rgb_w = rgb_shape[-1], rgb_shape[-3], rgb_shape[-2]
        depth_chan, depth_h, depth_w = depth_shape[-1], depth_shape[-3], depth_shape[-2]

        # Rete per le immagini RGB
        self.rgb_net = nn.Sequential(
            nn.Conv2d(rgb_chan, 16, kernel_size=5, stride=2),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, stride=2),
            nn.ReLU(),
            nn.Flatten(),
        )
        
        # Rete per le informazioni di profondità
        self.depth_net = nn.Sequential(
            nn.Conv2d(depth_chan, 8, kernel_size=5, stride=2),
            nn.ReLU(),
            nn.Conv2d(8, 16, kernel_size=3, stride=2),
            nn.ReLU(),
            nn.Flatten(),
        )

        # Calcola la dimensione finale delle feature
        with torch.no_grad():
            dummy_rgb = torch.zeros((1, rgb_chan, rgb_h, rgb_w))
            dummy_depth = torch.zeros((1, depth_chan, depth_h, depth_w))
            rgb_out_dim = self.rgb_net(dummy_rgb).shape[1]
            depth_out_dim = self.depth_net(dummy_depth).shape[1]

        self._features_dim = rgb_out_dim + depth_out_dim
        

    def forward(self, observations: dict) -> torch.Tensor:
        rgb = observations["rgb_image"].squeeze(0).permute(0, 3, 1, 2)  # (B, H, W, C) → (B, C, H, W)
        depth = observations["depth_image"].squeeze(0).permute(0, 3, 1, 2)

        rgb_feat = self.rgb_net(rgb)
        depth_feat = self.depth_net(depth)

        return torch.cat([rgb_feat, depth_feat], dim=1)
