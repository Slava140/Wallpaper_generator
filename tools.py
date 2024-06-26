import datetime

import cv2
import numpy as np
from perlin_numpy import generate_perlin_noise_2d


def get_noise_0_1(width: int, height: int, seed: int | None = None):
    np.random.seed(seed)
    noise = generate_perlin_noise_2d((height, width), (1, 1))
    return (noise + 1) / 2


def get_noise_0_255(width: int, height: int, seed: int | None = None):
    noise = get_noise_0_1(width, height, seed)
    return (noise * 255).astype(np.uint8)


def colorize(array_0_1: np.ndarray, rgb_color: np.ndarray):
    color = rgb_color[::-1]
    new_array_shape = (*array_0_1.shape, 3)
    return np.outer(array_0_1, color).astype(np.uint8).reshape(new_array_shape)


def save(image: np.ndarray, filename: str):
    cv2.imwrite(f'{filename}', image, [cv2.IMWRITE_PNG_COMPRESSION, 0])


def create_background(width: int, height: int,
                      color: np.ndarray,
                      seed: int | None = None):
    noise_0_1 = get_noise_0_1(width=width, height=height, seed=seed)
    return colorize(noise_0_1, color)


def is_iso_date(date: str):
    try:
        datetime.date.fromisoformat(date)
        return True
    except ValueError:
        return False
