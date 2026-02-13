# Pushups Tracker Instructions

- Open config.py and update config_dict with your choice of pixela username, token, graph id, and graph name. 
- Update config_dict with your min and max reps per set, min and max random targets, and the desired rest interval duration in seconds. 
- To track pushups using pixela API, use run_setup.py to create a pixela account and add your graph. 
- To save pushups log to a sqllite database, run database.py. 
- When you run main.py, it will ask for a target number of reps, or it will generate a random target within the defined min / max values.
- It breaks the target reps into sets of random size, and will alert you when the rest interval is over, as well as how many reps are in the next set. 
