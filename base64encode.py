import base64

def give64String():
    image = open('subject.jpg', 'rb')  # open binary file in read mode
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    almostRetString = str(image_64_encode)


    retString = almostRetString.replace("\\n", ",")
    retRetString = retString.replace(",", "")
    finString = retRetString.split("'")

    return finString[1]

