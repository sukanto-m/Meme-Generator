"""The meme engine to draw text on images."""

import os
import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """Draw text on the image."""

    def __init__(self, out_dir):
        """Initialise variables."""
        self.out_dir = out_dir

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

    def generate_meme(self, img_path, text, author, width=500) -> str:
        """Generate the meme."""
        img = Image.open(img_path)
        if width is not None:
            if width > 500:
                width = 500
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)
        if text is not None:
            draw = ImageDraw.Draw(img)
            fnt = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', 20)
            draw.text((5, 5), f'"{text}" - {author}', font=fnt, fill='white')

        rand_num = random.randint(0, 1000)
        out_path = os.path.join(self.out_dir, f'./{rand_num}.jpg')
        img.save(out_path)
        return out_path
