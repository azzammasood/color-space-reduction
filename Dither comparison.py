from PIL import Image
import colorsys

def main():
    widenBrightnessSearchRange = True  # If true, color intiation within the same hue range will be accepted, resulting in more masks but a more accurate albedo representation
    widenHueSearchRange = False  # This was a test, don't set to true
    regardSaturation = True  # Gives more accurate masks, but more of them,

    # Python's palette
    MyImageTrueColor = Image.open('input.jpg')
    MyImageDithered = MyImageTrueColor.convert(mode='P',
        colors=64,
        dither=1,
        palette = 1
        )
    MyImageTrueColor = MyImageTrueColor.convert(mode='P',
        dither=0)

    im2 = MyImageDithered.getpalette()

    dithered = []
    for i in im2:
        if i != 0:
            dithered.append(i)
    python_palette = []
    for i in range(len(dithered)):
        if (i % 3) == 2:
            python_palette.append(tuple(im2[i - 2:i + 1]))
    print(len(python_palette))
    print(python_palette)

    python_tags = []

    for color in python_palette:
        tag = getColorTag(color, widenBrightnessSearchRange, widenHueSearchRange, regardSaturation)
        python_tags.append(tag)

    python_tags = sorted(python_tags)
    print(python_tags)

    # Photoshop's palette
    print("\n Original palette:")
    im2 = MyImageTrueColor.getpalette()

    dithered = []
    for i in im2:
        if i != 0:
            dithered.append(i)
    python_palette = []
    for i in range(len(dithered)):
        if (i % 3) == 2:
            python_palette.append(tuple(im2[i - 2:i + 1]))
    print(len(python_palette))
    print(python_palette)

    photoshop_tags = []

    for color in python_palette:
        tag = getColorTag(color, widenBrightnessSearchRange, widenHueSearchRange, regardSaturation)
        photoshop_tags.append(tag)


    difference = list(set(python_tags) - set(photoshop_tags))
    print("\n difference: ", difference)



def getColorTag(color, widenBrightnessSearchRange, widenHueSearchRange, regardSaturation):
    red_percentage = color[0] / float(255)
    green_percentage = color[1] / float(255)
    blue_percentage = color[2] / float(255)


    # get hsv percentage: range (0-1, 0-1, 0-1)
    color_hsv_percentage = colorsys.rgb_to_hsv(red_percentage, green_percentage, blue_percentage)

    # get normal hsv: range (0-360, 0-255, 0-255)
    hue = round(360 * color_hsv_percentage[0])
    saturation = round(100 * color_hsv_percentage[1])
    brightness = round(100 * color_hsv_percentage[2])
    # color_hsv = (hue, saturation, brightness)

    tag = ""

    if(widenHueSearchRange):
        if(hue < 10): tag = "10"
        elif(hue < 20): tag = "20"
        elif(hue < 30): tag = "30"
        elif(hue < 40): tag = "40"
        elif(hue < 50): tag = "50"
        elif(hue < 60): tag = "60"
        elif(hue < 70): tag = "70"
        elif(hue < 80): tag = "80"
        elif(hue < 90): tag = "90"
        elif(hue < 100): tag = "100"
        elif(hue < 110): tag = "110"
        elif(hue < 120): tag = "120"
        elif(hue < 130): tag = "130"
        elif(hue < 140):  tag = "140"
        elif(hue < 150): tag = "150"
        elif(hue < 160): tag = "160"
        elif(hue < 170): tag = "170"
        elif(hue < 180): tag = "180"
        elif(hue < 190): tag = "190"
        elif(hue < 200): tag = "200"
        elif(hue < 210): tag = "210"
        elif(hue < 220): tag = "220"
        elif(hue < 230): tag = "230"
        elif(hue < 240):  tag = "240"
        elif(hue < 250): tag = "250"
        elif(hue < 260): tag = "260"
        elif(hue < 270): tag = "270"
        elif(hue < 280): tag = "280"
        elif(hue < 290): tag = "290"
        elif(hue < 300): tag = "300"
        elif(hue < 310): tag = "310"
        elif(hue < 320): tag = "320"
        elif(hue < 330): tag = "330"
        elif(hue < 340): tag = "340"
        elif(hue < 350): tag = "350"
        elif(hue < 360): tag = "360"
        else: tag = "0"
    else:
        if(hue < 10): tag = "Red"
        if(hue < 20):
            if(saturation < 50): tag = "Brown"
            else: tag = "Red-Orange"
        elif(hue < 40):
            if(saturation < 50): tag = "Brown"
            else: tag = "Orange"
        elif(hue < 50): tag = "Orange-Yellow"
        #elif(hue < 60): tag = "Yellow"
        #elif(hue < 80): tag = "Yellow-Green"
        elif(hue < 80): tag = "Yellow"
        #elif(hue < 140): tag = "Green"
        #elif(hue < 169): tag = "Green-Cyan"
        elif(hue < 169): tag = "Green"
        #elif(hue < 200): tag = "Cyan"
        #elif(hue < 220): tag = "Cyan-Blue"
        elif(hue < 220): tag = "Cyan"
        #elif(hue < 240): tag = "Blue"
        #elif(hue < 280): tag = "Blue-Magenta"
        elif(hue < 280): tag = "Blue"
       # elif(hue < 320): tag = "Magenta"
        #elif(hue < 330): tag = "Magenta-Pink"
        elif(hue < 330): tag = "Magenta"
        #elif(hue < 345): tag = "Pink"
        #elif(hue < 355): tag = "Pink-Red"
        else: tag = "Red"

    if(brightness < 25): tag = "Black-" + tag
    elif(brightness > 75):
        if(saturation < 33): tag = "White-" + tag

    if(regardSaturation):
        if(saturation < 10): tag = "Gray-" + tag
        elif(saturation < 20): tag = "Desaturated-" + tag
        elif(saturation < 40): tag = "Medium-Desaturated-" + tag
        elif(saturation > 80): tag = "Highly-Saturated-" + tag
        elif(saturation > 60): tag = "Saturated-" + tag
    elif(saturation < 20): tag = "Gray"

    if(widenBrightnessSearchRange):
        if(brightness < 30):  tag = "Dark-" + tag
        elif(brightness < 40):  tag = "Medium-Dark-" + tag
        elif(brightness > 70): tag = "Light-" + tag
        elif(brightness > 60):  tag = "Medium-Light-" + tag
    else:
        if(brightness < 30):  tag = "Dark-" + tag
        elif(brightness > 60):  tag = "Light-" + tag

    return tag

main()