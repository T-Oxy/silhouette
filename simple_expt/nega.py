import cv2

# 画像の色反転
def nega(image):
    img = cv2.imread(image)
    # ネガポジ反転
    img2 = cv2.bitwise_not(img)
    cv2.imwrite("0_nega.jpg",img2)

nega("0.jpg")
