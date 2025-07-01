import torch, math


def has_fallen(env, ref_link="pelvis", thr=0.5)->torch.Tensor:
    robot = env.scene["robot"]  # Recupera l'entità robot dalla scena
    base_link = robot.find_bodies(ref_link) # link di riferimento
    
    idx = base_link[0][0]  # ID del link di riferimento
    pos = robot.data.body_link_pos_w[:,idx,:] # Posizione del link di riferimento
    #print("Altezza del link ", str(base_link[1])," :", pos[:, 2].min().item())

    return pos[:, 2] < thr # tentativo gauss


def moving(env, ref_link="pelvis"):
    robot = env.scene["robot"] # Recupera l'entità robot dalla scena
    base_link = robot.find_bodies(ref_link)  # link di riferimento
    idx = base_link[0][0]  # ID del link di riferimento
    
    vel = robot.data.body_link_vel_w[:,idx,0:2] 
    speed = torch.norm(vel, dim=1)
    #print(f"Velocità del robot: {speed}")

    return torch.tanh(speed)
    

def position_error(env, command_name = "target") -> torch.Tensor:
    command_rel = env.command_manager.get_command(command_name) 
    distance = torch.norm(command_rel[:, :2], dim=1)  # Distanza dal target nel frame robot
    #print("Distanza dall'obiettivo: ", distance)

    return 1 - torch.tanh(distance)


def heading_error(env, command_name = "target") -> torch.Tensor:
    command_rel = env.command_manager.get_command(command_name) 
    heading_err = command_rel[:, 3]
    #print("Differenza di orientamento: ", heading_err)

    return 1 - torch.tanh(heading_err)


def target_reached(env,  command_name = "target", threshold=0.3):
    distance = position_error(env, command_name)   

    return distance < threshold


def out_of_manual_bound(env, max_dist=10, ref_link="pelvis"):
    robot = env.scene["robot"] # Recupera l'entità robot dalla scena
    base_link = robot.find_bodies(ref_link)  # link di riferimento
    idx = base_link[0][0] # ID del link di riferimento

    def_root_pos = robot.data.default_root_state[:,:3]
    env_pos =   env.scene.env_origins

    def_pos = def_root_pos + env_pos  # posizione di default del root link rispetto al mondo
    act_pos = robot.data.body_link_pos_w[:,idx,:] # posizione attuale del link di riferimento
    #print(f"Posizione di default: {def_pos} e posizione attuale: {act_pos}")  

    delta = torch.abs(act_pos[:, :2] - def_pos[:, :2])
    out = (delta > max_dist).any(dim=1).float()  # [B]
    return -out
    

def standing(env, ref_link="pelvis", tol=15) -> torch.Tensor:
    robot = env.scene["robot"]  # Recupera l'entità robot dalla scena
    base_link = robot.find_bodies(ref_link) # link di riferimento
    std_height = 0.8 
    
    idx = base_link[0][0]  # ID del link di riferimento
    pos = robot.data.body_link_pos_w[:,idx,:] # Posizione del link di riferimento

    return torch.exp(-tol * ((pos[:, 2] - std_height) ** 2)) # tentativo gauss # ricompensa quadratica 


def low_velocity(env, ref_link="pelvis", tol=1.0):
    robot = env.scene["robot"]
    idx = robot.find_bodies(ref_link)[0][0]
    vel = robot.data.body_link_vel_w[:, idx, 0:2]
    speed = torch.norm(vel, dim=1)

    return torch.exp(-tol * speed**2)





