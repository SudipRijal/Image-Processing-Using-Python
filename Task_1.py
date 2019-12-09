import numpy as np, cv2 as cv
from matplotlib import pyplot as plt
def rgb2grey(img):
    rgbImg = np.zeros((img.shape[0],img.shape[1],1),np.int32)
    for height in range(0,img.shape[0]):
        for width in range(0, img.shape[1]):
            rgbImg[height,width,0] =sum(img[height,width,:])/3
    return rgbImg
def histogram(img, title):
    if(img.shape[2] > 1):
        label = "RGB"

    else:
        label = ""

    colors =['red', 'blue', 'green']
    bins = [x for x in range(0, 256)]
    for channel in range(img.shape[2]):
        counts = np.zeros(256, np.int32)
        for height in range(0, img.shape[0]):

            intensity = 0
            for width in range(0, img.shape[1]):
                counts[img[height][width][channel]] += 1

        print()
        plt.bar(bins, counts, width=1, edgecolor='none',color =colors[channel])

    # counts, bins = np.histogram(img, range(257))
    # plot histogram centered on values 0..255

    # plt.xlim([-0.5, 255.5])

    # plt.figure(title)
    plt.legend(label)
    plt.title(title)
    # plt.show()

img = cv.imread("underexposed.jpg")
# plt.figure("underexposed.jpg")

histogram(img,"Under Exposed RGB Image")
# plt.show()
img = rgb2grey(img)
plt.figure(2)
# plt.show()
histogram(img,"Under Exposed Grey Image")
print()


img = cv.imread("overexposed.jpg")
plt.figure(3)
histogram(img, "Over Exposed RGB Image")
img = rgb2grey(img)
plt.figure(4)
histogram(img,"Over Exposed Grey Image")
print()