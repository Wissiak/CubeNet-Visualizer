import cv2
import numpy as np
from matplotlib import pyplot as plt

kernel_size = 3
reference_image = cv2.imread('model/reference.png', cv2.IMREAD_GRAYSCALE)

template_image = cv2.imread("model/template.png", cv2.IMREAD_GRAYSCALE)


#canny = cv2.imread('model/reference.png', cv2.COLOR_BGR2GRAY)
##gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
##canny = cv2.Canny(gray, 130, 255, 1)
#
#cnts = cv2.findContours(canny, 2,1)
#cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#
#
#canny2 = cv2.imread('model/template.png', cv2.COLOR_BGR2GRAY)
#canny2 = canny2[3:-3, 3:-3]
#cnts2 = cv2.findContours(canny2, 2,1)
#cnts2 = cnts2[0] if len(cnts2) == 2 else cnts2[1]

#cnts2 = sorted(cnts2, key = lambda x: len(x), reverse=True)
#cpy = cv2.imread('model/test4.png')
#cv2.drawContours(cpy,[cnts2[0]], 0, (0,255,0), 3)#

#cv2.imshow(f"result", cpy)
#cv2.waitKey(0)
#_, thresh_reference = cv2.threshold(reference_image, 127, 255, 0)
#_, thresh_template = cv2.threshold(template_image, 127, 255, 0)

# Find contours in both images
contours_reference, _ = cv2.findContours(reference_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours_template, _ = cv2.findContours(template_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#template_image = cv2.cvtColor(template_image, cv2.COLOR_GRAY2BGR)
#cv2.drawContours(template_image, contours_template, -1, (0, 0, 255), 2)

# Perform the matching with the convex hulls
hull_matches = [cv2.matchShapes(contours_ref, contours_template[0], 1, 0.0) for contours_ref in contours_reference]

# Find the best match among the convex hulls
min_hull_match_index = np.argmin(hull_matches)
best_hull_match_value = hull_matches[min_hull_match_index]

# Draw the best match convex hull on the original reference image
reference_image_color_hulls = cv2.cvtColor(reference_image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(reference_image_color_hulls, [contours_reference[min_hull_match_index]], -1, (0, 0, 255), 2)

# Save the result
cv2.imshow("Template image", template_image)
cv2.imshow('Reference Image', reference_image_color_hulls)
cv2.waitKey(0)


'''
method = cv2.TM_SQDIFF
(w, h) = template_image.shape
matching_result = cv2.matchTemplate(reference_image,template_image,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matching_result)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(reference_image, top_left, bottom_right, int(255), 3)

plt.subplot(121),plt.imshow(matching_result,cmap = 'gray')
plt.title('Matching matching_resultult'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(reference_image, cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

plt.show()
'''

exit(1)

distances = []
for i in range(len(cnt1)):
    ret = cv2.matchShapes(cnt1[i],cnt2[0], cv2.CONTOURS_MATCH_I2, 0.0)
    print(ret)
    distances.append(ret)

indices = sorted(range(len(distances)), key=lambda i: distances[i])
idx = indices[0]
cpy = img1.copy()
cv2.drawContours(cpy,[cnt1[idx]], 0, (0,255,0), 3)

print(len(cnt1[idx]))
print(len(cnt2[0]))

cv2.imshow(f"result {idx}", cpy)
cv2.waitKey(0)


cnts = sorted(cnt1, key = lambda x: len(x), reverse=True)
lengths = [len(c) for c in cnt1]
print(lengths)
exit(1)

for i, c in enumerate(cnts):
    cpy = image.copy()
    cv2.drawContours(cpy,[c], 0, (0,255,0), 3)

    cv2.imshow(f"result {i}", cpy)
    cv2.waitKey(0)