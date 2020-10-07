from PIL import Image
import random
import math
import seaborn as sns
from PIL import ImageColor

def generate_voronoi_diagram(width, height, num_cells, mean_x, stdv_x, mean_y, stdv_y, colorMap1, colorMap2):
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []

    # Define color palettes
    colors1 = sns.color_palette(colorMap1, 256)
    colors2 = sns.color_palette(colorMap2, 256)

    # Define sites and colors for each site
    for i in range(num_cells):
        nx.append(int(random.gauss(mean_x, stdv_x)))
        ny.append(int(random.gauss(mean_y, stdv_y)))

        if i%2 == 0:
            temp_color = colors1[random.randrange(256)]
        else:
            temp_color = colors2[random.randrange(256)]

        nr.append(int(temp_color[0]*256))
        ng.append(int(temp_color[1]*256))
        nb.append(int(temp_color[2]*256))

    # Create diagram
    for y in range(imgy):
        for x in range(imgx):
            dmin = math.hypot(imgx-1, imgy-1)
            j = -1
            for i in range(num_cells):
                d = math.hypot(nx[i]-x, ny[i]-y)
                if d < dmin:
                    dmin = d
                    j = i
            putpixel((x, y), (nr[j], ng[j], nb[j]))

    # Save image
    image.save(f"Voronoi Diagram.png", "PNG")

width = 2560
height = 1920
num_cells = 512
mean_x = 1280
stdv_x = 640
mean_y = 960
stdv_y = 480
colorMap1 = "GnBu"
colorMap2 = "YlOrRd"

generate_voronoi_diagram(width = width, height = height, num_cells = num_cells,
                         mean_x = mean_x, stdv_x = stdv_x, mean_y = mean_y,
                         stdv_y = stdv_y, colorMap1 = colorMap1,
                         colorMap2 = colorMap2)

