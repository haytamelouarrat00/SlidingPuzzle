import numpy as np
from PIL import Image
import random


def split_and_shuffle_image(image_path, count):
    # Load the image
    image = Image.open(image_path)
    width, height = image.size

    # Ensure the image is square
    if width != height:
        raise ValueError("Image must be square")

    # Calculate size of each tile
    grid_size = int(np.sqrt(count))
    if width % grid_size != 0:
        raise ValueError("Image dimensions must be divisible by the square root of count")
    tile_size = width // grid_size

    # Split image into tiles
    tiles = [image.crop((i * tile_size, j * tile_size, (i + 1) * tile_size, (j + 1) * tile_size))
             for j in range(grid_size) for i in range(grid_size)]

    # Remove one tile and shuffle
    tiles.pop()
    random.shuffle(tiles)

    # Create new image and place shuffled tiles
    new_image = Image.new('RGB', (width, height))
    for i, tile in enumerate(tiles):
        x = (i % grid_size) * tile_size
        y = (i // grid_size) * tile_size
        new_image.paste(tile, (x, y))

    return new_image


new_image = split_and_shuffle_image("img.png", 16)
new_image.show()
