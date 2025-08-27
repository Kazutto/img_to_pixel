from PIL import Image
from PIL import ImageOps
def pixelate(input_path, output_path, pixel_size):
    with Image.open(input_path) as im:
        scaler = im.resize((im.size[0] // pixel_size, im.size[1] // pixel_size), resample= Image.Resampling.NEAREST)
        scaler = scaler.resize(
            (im.size[0] + pixel_size, im.size[1] + pixel_size), Image.Resampling.NEAREST
        )

        ##upscaler
        result = scaler.resize(im.size)
        result.save(output_path)

i = input('Input File ("path.png") --> ')
o = input('Output Name ("name.png") --> ')
p = int(input('Pixel Factor (higher -> more pixel) --> '))

pixelate(i, o, p)