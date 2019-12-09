from laspy.file import File
import numpy as np
import matplotlib.pyplot as plt
import arcgis

# LasDatasetToRaster()
# arcgis.LasDatasetToRaster()

# arcgis.

inFile = File('17258975.las', mode='r')
rows = int(round(inFile.header.max[1]- inFile.header.min[1]))/8
cols = int(round(inFile.header.max[0]- inFile.header.min[0]))/8
rows = int(rows)
cols = int(cols)
a = np.zeros([rows, cols], dtype =float)
b = np.zeros([rows, cols])
lats = np.round(inFile.x%rows-1)
longs = np.round(inFile.y%cols-1)
for x,y,z in np.nditer([lats, longs, inFile.z]):
    a[int(x),int(y)] += 1
    b[int(x), int(y)] += z
print()
img = b/a
plt.figure()
plt.title("Raster Image")
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
print()
# x = plt.scatter(inFile.X, inFile.Y, s=20, alpha=0.1)
# plt.title('Scatter plot pythonspot.com')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
# print()
#
