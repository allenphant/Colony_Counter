import numpy as np
import cv2

# open the images
image = cv2.imread('./IMG_20250906_125817.jpg', cv2.IMREAD_COLOR)
mask1 = cv2.imread('./mask1.png', cv2.IMREAD_UNCHANGED)
mask2 = cv2.imread('./mask2.png', cv2.IMREAD_UNCHANGED)
assert image is not None and mask1 is not None and mask2 is not None, "Failed to load images."

# convert images to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
mask1_gray = cv2.cvtColor(mask1[:, :, :3], cv2.COLOR_BGR2GRAY)
mask2_gray = cv2.cvtColor(mask2[:, :, :3], cv2.COLOR_BGR2GRAY)
mask1_alpha = mask1[:, :, 3]
mask2_alpha = mask2[:, :, 3]

# matching the mask
result1 = cv2.matchTemplate(image_gray, mask1_gray, cv2.TM_CCOEFF_NORMED, mask=mask1_alpha)
result2 = cv2.matchTemplate(image_gray, mask2_gray, cv2.TM_CCOEFF_NORMED, mask=mask2_alpha)

# thresholding the result
threshold = 0.6
y_coords1, x_coords1 = np.where(result1 >= threshold)
y_coords2, x_coords2 = np.where(result2 >= threshold)

# draw rectangles on the matches
h1, w1 = mask1_gray.shape[:2]
for (x, y) in zip(x_coords1, y_coords1):
    cv2.rectangle(image, (x, y), (x + w1, y + h1), (0, 255, 0), 2)

h2, w2 = mask2_gray.shape[:2]
for (x, y) in zip(x_coords2, y_coords2):
    cv2.rectangle(image, (x, y), (x + w2, y + h2), (0, 255, 0), 2)

# save the result
cv2.imwrite('result.png', image)
