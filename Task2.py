import numpy as np, cv2 as cv
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import matplotlib
def histogramRGB(img, title):

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

    # plt.show()
    # plt.legend(label)
    plt.title(title)

def histogram(img, title):


    bins = [x for x in range(0, 10)]
    # for channel in range(img.shape[2]):
    counts = np.zeros(10, np.int32)
    for height in range(0, img.shape[0]):


        for width in range(0, img.shape[1]):
            counts[img[height][width]] += 1


    plt.bar(bins, counts, width=1, edgecolor='none')
    plt.title(title)
    # plt.show()
    # plt.legend(label)


# whiteImg = np.zeros((img.shape[0],img.shape[1],img.shape[2]),dtype=np.int)
# whiteImg.fill(255)
# cv.imwrite('Background.jpg', whiteImg)
def rgb2grey(img):
    rgbImg = np.zeros((img.shape[0],img.shape[1]),np.int32)
    for height in range(0,img.shape[0]):
        for width in range(0, img.shape[1]):
            rgbImg[height,width] =sum(img[height,width,:])/3
    return rgbImg

# print()

img = cv.imread("bottle.jpg")
img1 = cv.imread('Background.jpg')
subtract = img1-img
thershold = 20
subtract = rgb2grey(subtract)
for height in range(0,img1.shape[0]):
    for width in range(0,img1.shape[1]):
        if subtract[height,width] < thershold:
            subtract[height, width] = 0
        else:
            subtract[ height, width] = 1
plt.figure(1)
plt.imshow(img)
plt.title("Original Image With Background")
# plt.show()
plt.figure(2)

plt.imshow(subtract, cmap=plt.cm.gray)
plt.title("Binarized Image")
# plt.show()
plt.figure(3)

histogram(subtract,"Binarized Image Histogram")
plt.figure(4)
histogramRGB(img, "Original Image Histogram")
plt.show()