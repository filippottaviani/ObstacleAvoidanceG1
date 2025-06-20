from stable_baselines3.sac.policies import SACPolicy
from typing import Dict

from models.rgbd_feat_extr import RGBDCNNFeatureExtractor 



class CustomSACPolicy(SACPolicy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Registra la rete personalizzata per SB3
def get_custom_sac_policy(features_dim: int = 256) -> Dict:
    return {
        "features_extractor_class": RGBDCNNFeatureExtractor,
        "features_extractor_kwargs": {"features_dim": features_dim},
        "net_arch": {"pi": [256, 256], "qf": [256, 256]},  # puoi cambiare
    }
