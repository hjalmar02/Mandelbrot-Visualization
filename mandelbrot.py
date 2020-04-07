from numpy import complex, array
import sys
from utils import OptionMenu, ProgressBar
from datetime import date
from itertools import count
import os.path


def mandelbrot(c, n=100, r_factor=1, g_factor=0.5, b_factor=0.5):
    z = 0
    for i in range(n):
        if abs(z) > 2:
            red = int(255 * i / n * r_factor)
            green = int(255 * i / n * g_factor)
            blue = int(255 * i / n * b_factor)
            return (red, green, blue)
        z = z ** 2 + c
    return (0, 0, 0)


if __name__ == "__main__":
    from PIL import Image

    resolutions = ['128x128', '256x256', '512x512', '1024x1024', '2048x2048', '4096x4096', '8192x8192', '16384x16384',
                   '480x360', '1920x1080', '2560x1440', '3840x2160']
    options = OptionMenu(resolutions)
    size = {
        '128x128': (128, 128),
        '256x256': (256, 256),
        '512x512': (512, 512),
        '1024x1024': (1024, 1024),
        '2048x2048': (2048, 2048),
        '4096x4096': (4096, 4096),
        '8192x8192': (8192, 8192),
        '16384x16384': (16384, 16384),
        '480x360': (480, 360),
        '1920x1080': (1920, 1080),
        '2560x1440': (2560, 1440),
        '3840x2160': (3840, 2160)
    }[options.input("Resolution [<->]:")]
    WIDTH = size[0]
    HEIGHT = size[1]
    SCALE = WIDTH // 0.05  # WIDTH // 2.5
    X_OFFSET = -1 # -0.5
    Y_OFFSET = 0.25    # 0

    img = Image.new('RGB', (WIDTH, HEIGHT))
    pixels = img.load()

    progress = ProgressBar(40, WIDTH * HEIGHT)
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            progress.current = x * HEIGHT + y
            progress.update()
            x1 = (x / SCALE) - ((WIDTH / 2) / SCALE) + X_OFFSET
            y1 = (y / SCALE) - ((HEIGHT / 2) / SCALE) + Y_OFFSET
            pixels[x, y] = mandelbrot(complex(x1, y1), 1000)

    for i in count():
        if os.path.isfile(f'mandelbrot{i}.png'):
            continue
        else:
            img.save(f'mandelbrot{i}.png')
            break
    img.show()
