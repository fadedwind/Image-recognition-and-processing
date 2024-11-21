import cv2

"""读取彩色图片"""
image = cv2.imread("photo_2024-10-10_10-55-48.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.cvColor(grayImage, 60, 120)
cv2.imshow("Rew Image", image)
cv2.imshow("Edges Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()