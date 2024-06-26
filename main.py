import ctypes
import datetime
import os
import random

import numpy as np

from tools import create_background, save, is_iso_date

colors = np.array([
    [51, 76, 17],
    [118, 140, 69],
    [175, 192, 155],
    [174, 197, 113],
    [33, 111, 117],
    [56, 117, 91],
    [140, 157, 120],
    [220, 184, 161],
    [1, 49, 92],
    [0, 68, 124],
    [47, 111, 174],
    [181, 128, 137],
    [128, 101, 146],
    [105, 0, 3],
    [240, 110, 74],
    [240, 185, 174]
])
save_dir = 'C:\\Users\\Public\\Pictures'
today = datetime.date.today()
date_of_remove = today - datetime.timedelta(days=7)

today_filename = f'{today}.png'
date_of_remove_filename = f'{date_of_remove}.png'

path_to_today_background = f'{save_dir}\\{today_filename}'

today_file_exist = False
for file in os.listdir(save_dir):
    filename, extension = os.path.splitext(file)
    if extension != '.png' or not is_iso_date(filename):
        continue

    file_create_date = datetime.date.fromisoformat(filename)
    if file_create_date <= date_of_remove:
        os.remove(f'{save_dir}\\{file}')

    elif file_create_date == today:
        today_file_exist = True

if not today_file_exist:
    color = random.choice(colors)
    background = create_background(width=1920, height=1080, color=color)
    save(background, path_to_today_background)


ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_today_background, 3)


# 12B7D610257971F25F70926451BE58E6 Secret Key for fusion brain
