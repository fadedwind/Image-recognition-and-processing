import cv2
import matplotlib.pyplot as plt

# 读取彩色图片
image = cv2.imread("photo_2024-10-10_10-55-48.jpg")

# 应用高斯模糊
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# 使用 matplotlib 显示图像
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Blurred Image')
plt.axis('off')  # 不显示坐标轴
plt.show()