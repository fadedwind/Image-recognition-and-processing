import cv2
import matplotlib.pyplot as plt

# 读取彩色图片
image = cv2.imread("photo_2024-10-10_10-55-48.jpg")

# 转换为灰度图像
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用 matplotlib 显示图像
plt.imshow(grayImage, cmap='gray')
plt.title('Gray Image')
plt.axis('off')  # 不显示坐标轴
plt.show()