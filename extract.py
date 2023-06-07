from PIL import Image


def extract_data(image_path):
    encoded_message = ""
    image = Image.open(image_path, "r")

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            rgb = image.getpixel((x, y))
            r, g, b = rgb[0], rgb[1], rgb[2]
            r_bin = format(r, '08b')[-2:]
            g_bin = format(g, '08b')[-2:]
            b_bin = format(b, '08b')[-2:]
            encoded_message += r_bin + g_bin + b_bin
    byte_message = []
    for i in range(0, len(encoded_message), 8):
        byte = encoded_message[i:i+8]
        byte_message.append(byte)
    message = ""
    for byte in byte_message:
        try:
            char = chr(int(byte, 2))
            message += char
        except UnicodeEncodeError:
            message += "\\u" + byte
    return message


retrieved_message = extract_data("modified.png")
print("Retrieved message:")
print(retrieved_message.encode("unicode_escape").decode("utf-8"))
