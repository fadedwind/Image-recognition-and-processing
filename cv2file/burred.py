# 灰度化，滤波，边缘检测

import cv2

"""读取彩色图片"""

image = cv2.imread("photo_2024-10-10_10-55-48.jpg")

burred_Image = cv2.GaussianBlur(image, (5,5), 0)

#show the result

cv2.imshow("Gray Image", burred_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()