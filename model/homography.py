import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("model/template1.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('model/template.png')
template = template.astype(np.uint8)
img_gray = img_gray.astype(np.uint8)

height, width = template.shape[:2]

edges = cv2.Canny(template, 200, 250)
ght = cv2.createGeneralizedHoughGuil()
ght.setTemplate(edges)

ght.setMinDist(100)
ght.setMinAngle(0)
ght.setMaxAngle(360)
ght.setAngleStep(1)
ght.setLevels(360)
ght.setMinScale(1)
ght.setMaxScale(1.3)
ght.setScaleStep(0.05)
ght.setAngleThresh(100)
ght.setScaleThresh(100)
ght.setPosThresh(100)
ght.setAngleEpsilon(1)
ght.setLevels(360)
ght.setXi(1)

positions = ght.detect(img_gray)[0][0]

for position in positions:
    center_col = int(position[0])
    center_row = int(position[1])
    scale = position[2]
    angle = int(position[3])

    found_height = int(height * scale)
    found_width = int(width * scale)

    rectangle = ((center_col, center_row),
                    (found_width, found_height),
                    angle)

    box = cv2.boxPoints(rectangle)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

    for i in range(-2, 3):
        for j in range(-2, 3):
            img[center_row + i, center_col + j] = 0, 0, 255

cv2.imwrite("results.png", img)

'''
sift = cv.SIFT_create(
    nfeatures=10000,
    contrastThreshold=0.001,
    edgeThreshold=20,
    sigma=1.5,
    nOctaveLayers=16
)
trainPoints = sift.detect(trainImage, None)
queryPoints = sift.detect(queryImage, None)

_, trainDescriptors = sift.compute(trainImage, trainPoints)
_, queryDescriptors = sift.compute(queryImage, queryPoints)

matcher = cv.BFMatcher_create(cv.NORM_L2, crossCheck=True)
matches = matcher.match(queryDescriptors, trainDescriptors)
sortedMatches = sorted(matches, key = lambda x:x.distance)
print('{} matches found'.format(len(matches)))

pltImage = cv.drawMatches(queryImage, queryPoints, trainImage, trainPoints, sortedMatches[:400], queryImage, flags=2)
plt.imshow(pltImage)
plt.title('Brute force matching result')
plt.show()
'''