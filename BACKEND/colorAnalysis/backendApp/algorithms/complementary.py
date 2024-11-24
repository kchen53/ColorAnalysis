from conversion import *

def complementary_color(hue):
    hue = hue + 180

    if hue > 360:
        hue = hue - 360
    
    return round(hue)

#Testing
r, g, b = Hex_To_RGB("#FF5733")
hue, saturation, value = RGB_To_HSV(r, g, b)
print(r, g, b)
print(hue, saturation, value)
print(complementary_color(hue))