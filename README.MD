# ObstacleAvoidanceG1
Progetto di tesi magistrale in Ingegneria Robotica. Progettazione e implementazione di un algoritmo di obstacle avoidance per un robot umanoide (Unitree G1) attraverso tecniche di reinforcement learning e addestramento in ambiente simulato Isaac Sim.

## Organizzazione cartelle 
Il progetto è organizzato in diverse cartelle per esigenze di modularità e chiarezza. Di seguito, si illustra la disposizione finale dell'ambiente:

- **_agent_**: racchiude il file di configurazione dell'agente con la sua architettura, la sua politica e le parametrizzazionei per l'addestramento.
- **_assets_**: contiene le descrizioni USD delle varianti del G1.
- **_checkpoints_**: a sua volta racchiude _logs_ e _model_ in cui vengono salvate rispettivamente i log di simulazione e il modello finale derivante dall'addestramento. Questa cartella non è presente nella repository per motivi di spazio.
- **_managers_**: raccoglie, per ogni task, tutti i manager per la struttura ManagerBased (action, command, curriculum, event, observation, reward e termination).
- **_models_**: ospita modelli di computer vision utilizzati per contribuire alle osservazioni.
- **_robot_**: contiene i file di configurazione del robot e dei suoi attuatori.
- **_scenes_**: raccoglie le descrizioni degli scenari di simulazione.
- **_scripts_**: ci sono gli script di avvio per l'addestramento e per il test.
- **_sensors_**: ospita le descrizioni dei sensori montati sul robot.
- **_task_**: contiene la caratterizzazione e la registrazinoe dei tre task: locomozione, navigazione ed evitamento ostacoli.