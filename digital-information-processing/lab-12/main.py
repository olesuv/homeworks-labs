import cv2
from matplotlib import pyplot as plt

# Зчитуємо зображення
logo = cv2.imread("marker.jpg")
img = cv2.imread("background.jpg")

# Отримуємо розміри зображень
(wH, wW) = logo.shape[:2]
(h, w) = img.shape[:2]

# Обчислюємо координати для накладення маркера
startY = h - wH - 10
endY = h - 10
startX = w - wW - 10
endX = w - 10

# Вирізаємо область для маркера
destination = img[startY:endY, startX:endX]

# Змінюємо розміри зображення logo
logo_resized = cv2.resize(logo, (destination.shape[1], destination.shape[0]))

# Застосовуємо змінення за допомогою addWeighted
result = cv2.addWeighted(destination, 1, logo_resized, 0.7, 0)

# Замінюємо вихідну область зображення результатом
img[startY:endY, startX:endX] = result

# Зберігаємо результат
cv2.imwrite("watermarked.jpg", img)

# Показуємо зображення за допомогою matplotlib
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.show()

