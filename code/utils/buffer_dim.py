# dimensioni rgbd e lidar
rgb_x = 1920
rgb_y = 1080
depth_x = 1280
depth_y = 720
vision = True

# feature extraction
rgb_feat = 128
depth_feat = 128
lidar_feat = 128
feat_extr = False

# dimensioni osservazioni
rgb_dim = rgb_x * rgb_y
depth_dim = depth_x * depth_y
joint_pos = 12
joint_vel = 12
imu_vel_dim = 3
imu_acc_dim = 3
lidar_dim = 6144
target_dim = 4

if vision:
    if feat_extr: 
        obs_dim = rgb_feat + depth_feat + joint_pos + joint_vel + imu_acc_dim + imu_vel_dim + lidar_feat + target_dim
    else:
        obs_dim = rgb_dim + depth_dim + joint_pos + joint_vel + imu_acc_dim + imu_vel_dim + lidar_dim + target_dim 
else:
    obs_dim = joint_pos + joint_vel + imu_acc_dim + imu_vel_dim + target_dim 
action_dim = 12
num_envs = 8192
buffer_size = 2_000_000
bytes_per_element = 4  
reward_dim = 4
done_dim = 2

num_elements = buffer_size * (obs_dim + obs_dim + action_dim + reward_dim + done_dim) * num_envs
mem_bytes = num_elements * bytes_per_element
mem_GB = mem_bytes / (1024**3)
mem_TB = mem_bytes / (1024**4)
print(f"Il buffer contiene {num_elements:.0f} elementi.")
print(f"Memoria necessaria: {mem_GB:.1f} GB equivalente a circa {mem_TB:.1f} TB")
