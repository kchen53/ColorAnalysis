
def Hex_Alpha(character):
    hexAlpha = {
        "A": 10, "a": 10,
        "B": 11, "b": 11,
        "C": 12, "c": 12,
        "D": 13, "d": 13,
        "E": 14, "e": 14,
        "F": 15, "f": 15
     }
    
    if character.isalpha():
     if character in hexAlpha:
          return hexAlpha[character]
    else:
        return character

def Hex_To_RGB(hexString):
    if hexString[0] == "#":
        hexString = hexString[1:]
    
    if len(hexString) != 6:
         return -1, -1, -1

    r, g, b = hexString[0:2], hexString[2:4], hexString[4:6]

    r = int(Hex_Alpha(r[0]) * 16 + Hex_Alpha(r[1]))
    g = int(Hex_Alpha(g[0]) * 16 + Hex_Alpha(g[1]))
    b = int(Hex_Alpha(b[0]) * 16 + Hex_Alpha(b[1]))

    return r, g, b




    
