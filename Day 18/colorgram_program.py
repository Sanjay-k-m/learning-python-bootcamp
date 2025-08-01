import colorgram
def get_colors():
    colors = colorgram.extract('image.jpg',-1)
    color_array = []
    for color in colors:
        r =color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = (r,g,b)
        color_array.append(rgb)

    return color_array