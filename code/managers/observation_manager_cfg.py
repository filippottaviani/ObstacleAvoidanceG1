from isaaclab.managers import ObservationGroupCfg as ObsGroup
from isaaclab.managers import ObservationTermCfg as ObsTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.utils import configclass
import isaaclab.envs.mdp.observations as obs
from managers.mdp.mdp_custom import lidar_pc


@configclass
class ObservationsCfg:
    
    @configclass
    class PolicyCfg(ObsGroup):
        # observation terms (order preserved)
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
                    name= "rgbd_camera"
                ),
                "data_type": "rgb"
            }
        )
        
        # RGB-D camera (depth)
        depth_image = ObsTerm(
            func= obs.image,
            params={
                "sensor_cfg":  SceneEntityCfg(
                    name= "rgbd_camera"
                ),
                "data_type": "depth"
            }
        )
    
        # non supportato??? https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.envs.mdp.html#isaaclab.envs.mdp.observations.image
        # LiDAR point cloud
        lidar_points = ObsTerm(
            func=lidar_pc,
            params={
                "sensor_cfg": SceneEntityCfg(
                    name= "lidar"
                )
            }
        )

        def __post_init__(self) -> None:
            self.enable_corruption = False
            self.concatenate_terms = False

    policy: PolicyCfg = PolicyCfg()




    

