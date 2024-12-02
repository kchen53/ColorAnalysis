from complementary import *

# ----------------------------Testing for complementary function-------------------------------

#comparing rgb and hsv values for color and complementary color
print("---------------Color & Comp Color info----------------")
color = "#af30cf"
print("color: " + color)
print("r, g, b: ")
print(Hex_To_RGB(color))
print("h, s, v: ")
print(Hex_To_HSV(color))

print("--------------------------------------")

h, s, v = Hex_To_HSV(color)
comp_color = complementary_color(h, s, v)
print("complementary: " + comp_color)
print("r, g, b: ")
print(Hex_To_RGB(comp_color))
print("h, s, v: ")
print(Hex_To_HSV(complementary_color(h, s, v)))

print("\n")
print("---------------Test cases------------------")


#test function to check if complementary color is calculated properly
def comp_test(num, color, comp_color):

    hue, saturation, value = Hex_To_HSV(color)

    if complementary_color(hue, saturation, value) == comp_color:
        print(str(num) + '. true')
    else:
        print(str(num) + '. false')

#function to hold mutiple test functions
def tests():
    
    comp_test(1, "#FF5733", "33dbff")
    comp_test(2, "#ED5EEE", "5fee5e")
    comp_test(3, "#af30cf", "50cf30")
    comp_test(4, "#a5bc43", "5a43bc")
    comp_test(5, "#fa0552", "05faad")
    comp_test(6, "#2e58d1", "d1a72e")
    
#running tests
tests()
print("-------------Test cases end-----------------")
