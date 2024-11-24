import math

def Hex_Alpha(character):
    hex_Alpha = {
        "A": 10, "a": 10,
        "B": 11, "b": 11,
        "C": 12, "c": 12,
        "D": 13, "d": 13,
        "E": 14, "e": 14,
        "F": 15, "f": 15
     }
    
    if character.isalpha():
     if character in hex_Alpha:
          return hex_Alpha[character]
    else:
        return int(character)

def Hex_To_RGB(hex_String):
    if hex_String[0] == "#":
        hex_String = hex_String[1:]
    
    if len(hex_String) != 6:
         return -1, -1, -1

    r, g, b = hex_String[0:2], hex_String[2:4], hex_String[4:6]

    r = Hex_Alpha(r[0]) * 16 + Hex_Alpha(r[1])
    g = Hex_Alpha(g[0]) * 16 + Hex_Alpha(g[1])
    b = Hex_Alpha(b[0]) * 16 + Hex_Alpha(b[1])

    return r, g, b

def RGB_To_HSV(r, g, b):

    norm_R, norm_G, norm_B = r / 255, g / 255, b / 255

    norm_Max = max(norm_R, norm_G, norm_B)
    norm_Min = min(norm_R, norm_G, norm_B)

    delta = norm_Max - norm_Min

    if delta == 0:
        hue = 0
    
    if norm_Max == norm_R:
        hue = (norm_G - norm_B) / delta 
    elif norm_Max == norm_B:
        hue = ((norm_B - norm_R) / delta) + 2
    elif norm_Max == norm_G:
        hue = ((norm_R - norm_G) / delta) + 4
    
    if norm_Max == 0:
        saturation = 0
    else:
        saturation = delta / norm_Max

    value = norm_Max

    hue = round(hue * 60, 3)
    saturation = saturation * 100
    value = value * 100 
    
    return hue, saturation, value

# def HSV_To_RGB(hue, saturation, value):









    
