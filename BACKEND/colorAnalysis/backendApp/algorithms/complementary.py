from conversion import *

def complementary_color(hue):
    hue = hue + 180

    if hue > 360:
        hue = hue - 360
    
    return hue

#Testing
r, g, b = Hex_To_RGB("#FFFF00")
hue, saturation, value = RGB_To_HSV(r, g, b)
print(r, g, b)
print(hue, saturation, value)
print(complementary_color(hue))
print(HSV_To_RBG(complementary_color(hue), saturation, value))
print(RGB_To_Hex(r, g, b))
