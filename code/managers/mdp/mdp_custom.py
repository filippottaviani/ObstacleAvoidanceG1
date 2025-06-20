import torch


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









