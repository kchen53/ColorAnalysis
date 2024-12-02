import math

#helper for HEX_To_RBG
def Hex_Alpha(character):

    #hex A-F converts to 10-15
    hex_Alpha = {
        "A": 10, "a": 10,
        "B": 11, "b": 11,
        "C": 12, "c": 12,
        "D": 13, "d": 13,
        "E": 14, "e": 14,
        "F": 15, "f": 15
     }
    
    #checks if character is a letter and returns a number
    if character.isalpha():
     if character in hex_Alpha:
          num = hex_Alpha[character]
          return num
    else:
        num = int(character)
        return num

#helper for RBG_to_Hex
def Hex_Num(num):

    #hex 10-15 converts to A-F
    hex_num = {
        10 : "A", 10 : "a",
        11 : "B", 11 : "b",
        12 : "C", 12 : "c",
        13 : "D", 13 : "d",
        14 : "E", 14 : "e",
        15 : "F", 15 : "f"
     }
    
    #checks if num need to converted to letter and returns a string
    if num in hex_num:
        letter = hex_num[num]
        return letter
    
    if 0 <= num < 10:
        letter = str(num)
        return letter

#converts hex string to decimal rgb values
def Hex_To_RGB(hex_String):

    #edge cases
    if hex_String[0] == "#":
        hex_String = hex_String[1:]
    
    if len(hex_String) != 6:
         return -1, -1, -1

    #splits hex strings to hex r, g, b values
    r, g, b = hex_String[0:2], hex_String[2:4], hex_String[4:6]

    #converts hex r, g, b values to decimal r, g, b values
    r = Hex_Alpha(r[0]) * 16 + Hex_Alpha(r[1])
    g = Hex_Alpha(g[0]) * 16 + Hex_Alpha(g[1])
    b = Hex_Alpha(b[0]) * 16 + Hex_Alpha(b[1])

    return r, g, b

#converts decimal r, g, b values to a hex string
def RGB_To_Hex(r, g, b):

    #concating r, g, b hex values
    r = Hex_Num(math.floor(r / 16)) + Hex_Num(r % 16)
    g = Hex_Num(math.floor(g / 16)) + Hex_Num(g % 16)
    b = Hex_Num(math.floor(b / 16)) + Hex_Num(b % 16)

    hex = r + g + b

    return hex

#converts rgb values to hsv values
def RGB_To_HSV(r, g, b):

    #normalize r, g, b values to be within [0,1]
    normR, normG, normB = r / 255, g / 255, b / 255

    #conversion algo
    norm_Max = max(normR, normG, normB)
    norm_Min = min(normR, normG, normB)

    delta = norm_Max - norm_Min

    #determine hue
    if delta == 0:
        hue = 0
    
    if norm_Max == normR:
        hue = ((normG - normB) / delta) % 6
    elif norm_Max == normG:
        hue = ((normB - normR) / delta) + 2
    elif norm_Max == normB:
        hue = ((normR - normG) / delta) + 4
    
    #determine saturation
    if norm_Max == 0:
        saturation = 0
    else:
        saturation = delta / norm_Max

    #determine value
    value = norm_Max

    #convert hue to degree, and saturation and value to percentages
    hue = (hue / 6) % 1
    hue = hue * 360
    saturation = saturation * 100
    value = value * 100 
    
    return hue, saturation, value

#converts hsv values to rgb values
def HSV_To_RBG(hue, saturation, value):

    #normalize values
    saturation = saturation / 100
    value = value / 100

    #conversion algo
    chroma = value * saturation

    x = chroma * (1 - abs(((hue / 60) % 2) - 1))

    #calculating r, g, b based on hue angle
    if 0 <= hue < 60:
        R, G, B = chroma, x, 0
    elif 60 <= hue < 120:
        R, G, B = x, chroma, 0
    elif 120 <= hue < 180:
        R, G, B = 0, chroma, x
    elif 180 <= hue < 240:
        R, G, B = 0, x, chroma
    elif 240 <= hue < 300:
        R, G, B = x, 0, chroma
    elif 300 <= hue < 360:
        R, G, B = chroma, 0, x
    
    m = value - chroma

    #converting r, g, b values to be within [0, 255]
    r = round((R + m) * 255)
    g = round((G + m) * 255)
    b = round((B + m) * 255)

    return r, g, b

#converts hex to hsv values
def Hex_To_HSV(hex_string):

    r, g, b = Hex_To_RGB(hex_string)
    h, s, v = RGB_To_HSV(r, g, b)

    return h, s, v

#converts HSV to hex string
def HSV_To_Hex(h, s, v):

    r, g, b = HSV_To_RBG(h, s, v)
    hex_string = RGB_To_Hex(r, g, b)

    return hex_string




    









    
