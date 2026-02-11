# Pushups Tracker Instructions

- In main.py you can specify the min / max reps per set, and the duration of the rest interval.
- Option to save progress to a sqllite database.
- Option to save progress to pixela. You need to set up a user account and obtain a token and url for the API: https://pixe.la/. Put these in pixela_creds.yaml. 
- When you run main.py, it will ask for a target number of reps, or it will generate a random target within the defined min / max values.
- It breaks the target reps into sets of random size, and will alert you when the rest interval is over, as well as how many reps are in the next set. 
