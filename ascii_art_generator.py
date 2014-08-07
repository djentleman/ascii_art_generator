from PIL import Image
import PIL
import webbrowser
import Tkinter
import tkFileDialog

def getImage():
    root = Tkinter.Tk()
    root.withdraw()
    filename = tkFileDialog.askopenfilename()
    return filename

def greyscale(img):
    img = img.convert('LA')
    return img

def writeToFile(path, data):
    open(path, "w+").write(data)

def getChar(pixel):
    pixel = 255 - pixel
    if pixel < 25:
        return " "
    elif pixel < 50:
        return "-"
    elif pixel < 75:
        return "="
    elif pixel < 100:
        return "I"
    elif pixel < 125:
        return "i"
    elif pixel < 150:
        return "7"
    elif pixel < 175:
        return "P"
    elif pixel < 200:
        return "N"
    elif pixel < 225:
        return "W"
    else:
        return "M"


def main():
    # get image
    path = getImage()
    img = Image.open(path)
    # convert image to greyscale
    img = greyscale(img)
    #img.show()
    # resize img
    img = img.resize((128,128), PIL.Image.ANTIALIAS)
    pixels = img.load()
    dimensions = img.size
    art = ""
    # iterate through pixels, build up ascii art string
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            art += getChar(pixels[j, i][0])
        art += "\n"
    # write ascii art to file
    writeToFile("test.txt", "<p>" + art + "</p>")
    # open file in browser?
    # (opens in notepad but hey)
    webbrowser.open("test.txt", new=0)


if __name__ == "__main__":
    main()
