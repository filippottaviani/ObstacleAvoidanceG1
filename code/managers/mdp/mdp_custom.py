import torch, math

# ================== OBSERVATION ==================

def lidar_pc(env, sensor_cfg, num_points=2048):
    # Verifica che il nome del sensore esista nella scena
    if sensor_cfg.name not in env.scene.sensors:
        raise ValueError(f"LiDAR '{sensor_cfg.name}' non trovato nella scena. Sensori disponibili: {list(env.scene.sensors.keys())}")
    
    # Recupera il sensore lidar dalla scena
    lidar = env.scene.sensors[sensor_cfg.name]
    data = lidar.data

    all_points = []

    for i in range(env.num_envs):
        # Correzione dei numeri della point cloud
        pc_fixed = pc_number_fixer(data.ray_hits_w[0], num_points)

        # Matrici dei dati 
        Pl_w = data.pos_w[0] # posizione del lidar rispetto al mondo
        Rl_w = data.quat_w[0] # rotazione del lidar rispetto al mondo
        Ph_w = pc_fixed # punti colpiti dal lidar nel mondo

        # Orientamento trasposto del lidar 
        Rcw = quaternion_to_rotation_matrix_batch(Rl_w)  
        Rwc = Rcw.T

        # Differenza posizioni
        diff = Ph_w - Pl_w[None, :]  

        # Rotazione
        Ph_l = torch.matmul(diff, Rwc)

        # Aggiunta ai punti già calcolati
        all_points.append(Ph_l.flatten()) 
        
    result = torch.stack(all_points, dim=0)
    #print("lidar_points:", result.shape)

    return result


def quaternion_to_rotation_matrix_batch(q):
    x, y, z, w = q[0], q[1], q[2], q[3]

    R = torch.zeros((3, 3), device=q.device)
    R[0, 0] = 1 - 2*(y**2 + z**2)
    R[0, 1] = 2*(x*y - z*w)
    R[0, 2] = 2*(x*z + y*w)
    R[1, 0] = 2*(x*y + z*w)
    R[1, 1] = 1 - 2*(x**2 + z**2)
    R[1, 2] = 2*(y*z - x*w)
    R[2, 0] = 2*(x*z - y*w)
    R[2, 1] = 2*(y*z + x*w)
    R[2, 2] = 1 - 2*(x**2 + y**2)

    return R


def pc_number_fixer(pc, num_points):
    # rimuovi NaN o Inf
    valid_mask = torch.isfinite(pc).all(dim=-1)
    pc = pc[valid_mask]

    if pc.shape[0] >= num_points:
        # campiona
        idx = torch.randperm(pc.shape[0])[:num_points]
        points_sampled = pc[idx]
    else:
        # padding
        pad = num_points - pc.shape[0]
        padding = torch.zeros(pad, 3, device=pc.device)
        points_sampled = torch.cat([pc, padding], dim=0)

    return points_sampled 


def target_pos(env, command_name: str) -> torch.Tensor:
    return env.command_manager.get_command(command_name)


# ================== REWARD ==================

def has_fallen(env, ref_link="pelvis", height_thr=0.3):
    robot = env.scene["robot"]  # Recupera l'entità robot dalla scena
    base_link = robot.find_bodies(ref_link) # link di riferimento
    
    idx = base_link[0][0]  # ID del link di riferimento
    pos = robot.data.body_link_pos_w[:,idx,:] # Posizione del link di riferimento
    #print("Altezza del link ", str(base_link[1])," :", pos[:, 2].min().item())

    # Controllo altezza
    if (pos[:, 2].min().item()) < height_thr:
        print("Il robot è caduto!")
        return True
    else:
        return False


def moving(env, ref_link="pelvis", vel_thr=0.1):
    robot = env.scene["robot"] # Recupera l'entità robot dalla scena
    base_link = robot.find_bodies(ref_link)  # link di riferimento
    idx = base_link[0][0]  # ID del link di riferimento
    vel = robot.data.body_link_vel_w[:,idx,:]  # Posizione del link di riferimento

    # Calcola le velocità medie laterali
    velocity_x = vel[:, 0].mean()
    velocity_y = vel[:, 1].mean() 
    #print(f"Velocità del robot: x={velocity_x}, y={velocity_y}")

    if abs(velocity_x) > vel_thr or abs(velocity_y) > vel_thr:  
        return True
    else:
        return False
    

def position_error(env, command_name = "target") -> torch.Tensor:

    command_rel = env.command_manager.get_command(command_name) 
    distance = torch.norm(command_rel[:, :2], dim=1)  # Distanza dal target nel frame robot
    #print("Distanza dall'obiettivo: ", distance)

    return distance


def position_error_tanh(env, std: float, command_name = "target") -> torch.Tensor:
    distance = position_error(env, command_name)

    return 1 - torch.tanh(distance / std)


def target_reached(env,  command_name = "target", threshold=0.3):
    distance = position_error(env, command_name)   

    return distance < threshold


# ================== TERMINATION ==================

def out_of_manual_bound(env, max_dist=10, ref_link="pelvis"):
    robot = env.scene["robot"] # Recupera l'entità robot dalla scena
    base_link = robot.find_bodies(ref_link)  # link di riferimento
    idx = base_link[0][0] # ID del link di riferimento

    def_root_pos = robot.data.default_root_state[:,:3]
    env_pos =   env.scene.env_origins

    def_pos = def_root_pos + env_pos  # posizione di default del root link rispetto al mondo
    act_pos = robot.data.body_link_pos_w[:,idx,:] # posizione attuale del link di riferimento
    #print("Posizione di default:", def_pos)  
    #print("Posizione attuale:", act_pos)

    # compute any violations
    out_of_upper_limits = True if abs(act_pos[:, 0] - def_pos[:, 0]).max() > max_dist else False
    out_of_lower_limits = True if abs(act_pos[:, 1] - def_pos[:, 1]).max() > max_dist else False

    return out_of_upper_limits or out_of_lower_limits
    








