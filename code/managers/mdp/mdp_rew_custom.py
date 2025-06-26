import torch


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

    out_of_x_limits = True if abs(act_pos[:, 0] - def_pos[:, 0]).max() > max_dist else False
    out_of_y_limits = True if abs(act_pos[:, 1] - def_pos[:, 1]).max() > max_dist else False

    return out_of_x_limits or out_of_y_limits
    








