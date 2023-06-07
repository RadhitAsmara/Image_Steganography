from PIL import Image

message = "This is a secret message!"
image = Image.open("original.png", "r")


def read_file(message):
    byte_message = []
    for c in message:
        byte_message.append(format(ord(c), '08b'))
    splitByte_message = []
    for x in byte_message:
        splitByte_message.append(x[0:2])
        splitByte_message.append(x[2:4])
        splitByte_message.append(x[4:6])
        splitByte_message.append(x[6:8])
    for x in range(4):
        if (len(splitByte_message) % 3 != 0):
            splitByte_message.append('00')
        else:
            break
    return splitByte_message


binary = read_file(message)
OldImage = image
NewImage = OldImage.copy()

imgMode = NewImage.mode
pixel_Image = NewImage.size[0]*NewImage.size[1]
req_pixel = int(len(binary)/3)

index = 0
for x in range(NewImage.size[0]):
    for y in range(NewImage.size[1]):
        if (index < len(binary)):
            _rgb = NewImage.getpixel((x, y))
            _r = int(format(_rgb[0], '08b')[0:6]+binary[index], 2)
            _g = int(format(_rgb[1], '08b')[0:6]+binary[index+1], 2)
            _b = int(format(_rgb[2], '08b')[0:6]+binary[index+2], 2)
            NewImage.putpixel((x, y), (_r, _g, _b))
            index += 3
NewImage.save("modified.png", "PNG")
