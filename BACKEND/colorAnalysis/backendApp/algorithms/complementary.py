from conversion import *

#determines the complementary color based on hue and return the color's hex string
def complementary_color(hue, saturation, value):

    #find opposite color
    hue = hue + 180

    #to keep hue within color wheel range
    if hue > 360:
        hue = hue - 360
    
    #conversion algo to get hex string of complementary color
    compColor = HSV_To_Hex(hue, saturation, value)
    
    return compColor



