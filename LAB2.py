import PIL
from PIL import Image

img = Image.new('RGB', (540, 960), color='white')

pixels = img.load()

file = open("DS1.txt", "r")

for line in file:
    coord = line.split()
    coord[0] = int(coord[0])
    coord[1] = int(coord[1])

    pixels[coord[0], coord[1]] = (0, 0, 0)

file.close()

img.save('result.png')