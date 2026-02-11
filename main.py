import random
import time
import sqlite3
from datetime import datetime
# from beepy import beep
from tqdm import tqdm
from pixela import add_pixel
from gtts import gTTS
from playsound import playsound


target = input("Enter target number of reps, or enter R for random.")
if target.lower() == "r":
    target = random.randint(55, 105)
    print(f"Target number of reps: {target}")
else:
    target = int(target)

save_to_db = False
save_to_pixela = False
min_reps_per_set = 6  # int(input("Enter min reps per set."))
max_reps_per_set = 15  # int(input("Enter max reps per set."))
rest = 60

# TODO: exit early

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
    reps = random.randint(min_reps_per_set, max_reps_per_set)
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
    for i in tqdm(range(rest)):
        time.sleep(rest / 60)
    # random_sound_int = random.randint(1, 7)
    # beep(random_sound_int)

print(pushups_list)
date = datetime.now().strftime("%Y%m%d")

if save_to_db:
    db = sqlite3.connect("pushups.db")
    cursor = db.cursor()
    max_id = cursor.execute("SELECT MAX(id) from pushups").fetchone()[0]
    db_id = max_id + 1
    for i in range(0, len(pushups_list)):
        cursor.execute(f"INSERT INTO pushups VALUES ({db_id}, '{date}', {i + 1}, {pushups_list[i]})")
        db_id += 1
    db.commit()
    cursor.close()

if save_to_pixela:
    add_pixel(date, reps=sum(pushups_list))
