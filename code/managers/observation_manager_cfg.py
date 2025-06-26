from isaaclab.managers import ObservationGroupCfg as ObsGroup
from isaaclab.managers import ObservationTermCfg as ObsTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass
import isaaclab.envs.mdp.observations as obs
import managers.mdp.mdp_obs_custom as mdp_custom


@configclass
class ObservationsCfg:
    
    @configclass
    class PolicyCfg(ObsGroup):
        # Letture encoder
        joint_pos_rel = ObsTerm(func=obs.joint_pos_rel)
        joint_vel_rel = ObsTerm(func=obs.joint_vel_rel)

        '''# Contact 
        foot_contacts = ObsTerm(
            func=obs.imu_ang_vel,
            params={
                "asset_cfg": SceneEntityCfg(
                    name= "imu"
                )
            }
        )'''

        # IMU
        imu_ang_vel = ObsTerm(
            func=obs.imu_ang_vel,
            params={
                "asset_cfg": SceneEntityCfg(
                    name= "imu"
                )
            }
        )

        imu_lin_acc = ObsTerm(
            func=obs.imu_lin_acc,
            params={
                "asset_cfg": SceneEntityCfg(
                    name= "imu"
                )
            }
        )

        # RGB-D camera (rgb)
        rgb_image = ObsTerm(
            func= obs.image,
            params={
                "sensor_cfg":  SceneEntityCfg(
                    name= "rgb_camera"
                ),
                "data_type": "rgb"
            }
        )
        
        # RGB-D camera (depth)
        depth_image = ObsTerm(
            func= obs.image,
            params={
                "sensor_cfg":  SceneEntityCfg(
                    name= "depth_camera"
                ),
                "data_type": "depth"
            }
        )

        # LiDAR point cloud
        lidar_points = ObsTerm(
            func=mdp_custom.lidar_pc,
            params={
                "sensor_cfg": SceneEntityCfg(
                    name= "lidar"
                )
            }
        )

        # Assegnazione target
        target_position = ObsTerm(
            func=mdp_custom.target_pos,
            params={
                "command_name": "target"
            }
        )

        def __post_init__(self) -> None:
            self.enable_corruption = False
            self.concatenate_terms = False

    policy: PolicyCfg = PolicyCfg()




    

