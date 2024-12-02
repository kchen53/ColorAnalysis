from complementary import *

# ----------------------------Testing for complementary function-------------------------------
hex_string = "#af30cf"
print("color: " + hex_string)
print("r, g, b: ")
print(Hex_To_RGB(hex_string))
print("h, s, v: ")
print(Hex_To_HSV(hex_string))

print("\n")

h, s, v = Hex_To_HSV(hex_string)
print("complementary: ")
print(complementary_color(h, s, v))
print("h, s, v: ")
print(Hex_To_HSV(complementary_color(h, s, v)))

def test1():
    hue, saturation, value = Hex_To_HSV("#FF5733")

    if complementary_color(hue, saturation, value) == "33dbff":
       print('true')
    else:
        print('false')

def test2():
    hue, saturation, value = Hex_To_HSV("#ED5EEE")

    if complementary_color(hue, saturation, value) == "5fee5e":
        print('true')
    else:
        print('false')

def test3():
    hue, saturation, value = Hex_To_HSV("#af30cf")

    if complementary_color(hue, saturation, value) == "50cf30":
        print('true')
    else:
        print('false')

def test4():
    hue, saturation, value = Hex_To_HSV("#a5bc43")

    if complementary_color(hue, saturation, value) == "5a43bc":
        print('true')
    else:
        print('false')

def test5():
    hue, saturation, value = Hex_To_HSV("#fa0552")

    if complementary_color(hue, saturation, value) == "05faad":
        print('true')
    else:
        print('false')

def test6():
    hue, saturation, value = Hex_To_HSV("#2e58d1")

    if complementary_color(hue, saturation, value) == "d1a72e":
        print('true')
    else:
        print('false')

test1()
test2()
test3()
test4()
test5()
test6()