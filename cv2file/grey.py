# 灰度化，滤波，边缘检测

import cv2

"""读取彩色图片"""

image = cv2.imread("photo_2024-10-10_10-55-48.jpg")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()