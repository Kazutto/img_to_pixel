from PIL import Image

SNES_PALETTE = [
    (0, 0, 0),       # black
    (255, 255, 255), # white
    (128, 128, 128), # gray
    (200, 0, 0),     # red
    (0, 200, 0),     # green
    (0, 0, 200),     # blue
    (200, 200, 0),   # yellow
    (200, 100, 0),   # orange
    (255, 150, 200), # pink
    (150, 0, 200),   # purple
    (0, 200, 200),   # cyan
    (100, 50, 0),    # brown
    (150, 200, 150), # light green
    (200, 150, 100), # beige
    (50, 50, 150),   # dark blue
    (100, 100, 50),  # olive
]

def create_palette_image(palette):
    pal_img = Image.new("P", (16, 16))
    flat_palette = []
    for color in palette:
        flat_palette.extend(color)
    # Pad palette to 768 values (256 colors × 3 channels)
    flat_palette += [0] * (768 - len(flat_palette))
    pal_img.putpalette(flat_palette)
    return pal_img

def pixelate(input_path, output_path, pixel_size, snes=True):
    with Image.open(input_path) as im:
        scaler = im.resize((im.size[0] // pixel_size, im.size[1] // pixel_size), resample= Image.Resampling.NEAREST)
        scaler = scaler.resize(
            (im.size[0] + pixel_size, im.size[1] + pixel_size), Image.Resampling.NEAREST
        )

        ##upscaler
        result = scaler.resize(im.size)

        if snes:
            pal_img = create_palette_image(SNES_PALETTE)
            result = result.quantize(palette=pal_img)
        result.save(output_path)

i = input('Input File ("path.png") --> ')
o = input('Output Name ("name.png") --> ')
p = int(input('Pixel Factor (higher -> more pixel) --> '))

pixelate(i, o, p, snes=True)