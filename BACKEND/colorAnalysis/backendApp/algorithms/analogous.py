from conversion import *

def analogous_color(hue, saturation, value):

    #find analogous color
    hue_left = hue - 30
    hue_right = hue + 30

    #to keep hue within color wheel range
    if hue_left > 360:
        hue_left = hue_left - 360
    if hue_right > 360:
        hue_right = hue_right - 360
    
    #conversion algo to get hex value for each color
    main_color = HSV_To_Hex(hue, saturation, value)
    left_color = HSV_To_Hex(hue_left, saturation, value)
    right_color = HSV_To_Hex(hue_right, saturation, value)
    
    return main_color, right_color, left_color



# ----------------------------Testing for analogous function-------------------------------
h, s, v = Hex_To_HSV("#fa0552")
m, r, l = analogous_color(h, s, v)

print(m)
print(Hex_To_HSV(m))
print(Hex_To_RGB(m))

print(r)
print(Hex_To_HSV(r))
print(Hex_To_RGB(r))

print(l)
print(Hex_To_HSV(l))
print(Hex_To_RGB(l))

