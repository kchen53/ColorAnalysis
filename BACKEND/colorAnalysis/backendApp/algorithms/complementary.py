from conversion import *

#determines the complementary color based on hue and return the color's hex string
def complementary_color(hue, saturation, value):

    #find opposite color
    hue = hue + 180

    #to keep hue within color wheel range
    if hue > 360:
        hue = hue - 360
    
    #conversion algo to get hex string of complementary color
    r, g, b = HSV_To_RBG(hue, saturation, value)
    compColor = RGB_To_Hex(r, g, b)
    
    return compColor

#Testing
r, g, b = Hex_To_RGB("#FFFF00")
hue, saturation, value = RGB_To_HSV(r, g, b)
print(r, g, b)
print(hue, saturation, value)
print(complementary_color(hue, saturation, value))
print(RGB_To_Hex(r, g, b))
