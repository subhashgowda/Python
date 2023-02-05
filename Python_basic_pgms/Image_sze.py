def jpeg_res(filename):

    # open image for reading in binary mode
    with open(filename,'rb') as image_file:
        # height of image (in 2 bytes) is at 164th position
        image_file.seek(164)

        # read the 2 bytes
        a = image_file.read(2)

        # calculate height
        height = (a[0]<<8)+a[1]
        
        # next 2 bytes is width
        a = image_file.read(2)

        # calculate width
        width = (a[0] << 8) + a[1]

    print("The resolution of the image is",width,"x",height)


filename = "temp.jpg"
jpeg_res(filename)
