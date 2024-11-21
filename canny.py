import cv2
import matplotlib.pyplot as plt

# 读取彩色图片
image = cv2.imread("photo_2024-10-10_10-55-48.jpg")

# 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用 Canny 边缘检测
edges_image = cv2.Canny(gray_image, 60, 200)

# 使用 matplotlib 显示原始图像和边缘图像
plt.figure(figsize=(10, 5))

# 显示原始图像
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Raw Image')
plt.axis('off')  # 不显示坐标轴

# 显示边缘图像
plt.subplot(1, 2, 2)
plt.imshow(edges_image, cmap='gray')
plt.title('Edges Image')
plt.axis('off')  # 不显示坐标轴

plt.show()