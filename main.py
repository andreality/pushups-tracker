import random
import time
import sqlite3
from datetime import datetime
# from beepy import beep
from tqdm import tqdm
from pixela.pixels import add_pixel
from gtts import gTTS
from playsound import playsound
from config import config_dict


target = input("Enter target number of reps, or enter R for random.")
if target.lower() == "r":
    target = random.randint(config_dict['min_random_target'], config_dict['max_random_target'])
    print(f"Target number of reps: {target}")
else:
    target = int(target)


pushups_list = []
language = 'en'


def get_reps_input(reps):
    reps_done = input(f"Target reps for this set is {reps}. How many did you do?")
    try:
        reps_done = int(reps_done)
    except ValueError:
        reps_done = get_reps_input(reps)
    return reps_done


while sum(pushups_list) < target:
    remaining = target - sum(pushups_list)
    reps = random.randint(config_dict['min_reps_per_set'], config_dict['max_reps_per_set'])
    reps = min(reps, remaining)
    tts = gTTS(str(reps))
    tts.save("x.mp3")
    playsound("x.mp3")
    reps_done = get_reps_input(reps)
    pushups_list.append(reps_done)
    remaining = target - sum(pushups_list)
    if remaining == 0:
        break
    print(f"Total remaining: {remaining}")
    for i in tqdm(range(config_dict['rest'])):
        time.sleep(config_dict['rest'] / 60)
    # random_sound_int = random.randint(1, 7)
    # beep(random_sound_int)

print(pushups_list)
date = datetime.now().strftime("%Y%m%d")

if config_dict['save_to_db']:
    db = sqlite3.connect(config_dict['database_name'])
    cursor = db.cursor()
    max_id = cursor.execute("SELECT MAX(id) from pushups").fetchone()[0]
    if max_id is None:
        max_id = 0
    db_id = max_id + 1
    for i in range(0, len(pushups_list)):
        cursor.execute(f"INSERT INTO pushups VALUES ({db_id}, '{date}', {i + 1}, {pushups_list[i]})")
        db_id += 1
    db.commit()
    cursor.close()

if config_dict['save_to_pixela']:
    add_pixel(date, reps=sum(pushups_list))
